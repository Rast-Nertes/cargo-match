from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.cargo_request import CargoRequest, CargoRequestStatus
from app.models.match import Match, MatchStatus
from app.models.trip import Trip, TripStatus


class MatchingService:
    """Эвристическое сопоставление заявок с рейсами (включая обратные)."""

    @staticmethod
    def _normalize_city(name: str) -> str:
        return name.strip().lower()

    @classmethod
    def compute_score(
        cls,
        request: CargoRequest,
        trip: Trip,
    ) -> tuple[Decimal, bool, str | None]:
        req_origin = cls._normalize_city(request.origin_city)
        req_dest = cls._normalize_city(request.destination_city)
        trip_origin = cls._normalize_city(trip.origin_city)
        trip_dest = cls._normalize_city(trip.destination_city)

        score = Decimal("0")
        is_backhaul = False
        notes: list[str] = []

        if req_origin == trip_origin and req_dest == trip_dest:
            score += Decimal("80")
            notes.append("Прямое совпадение маршрута")
        elif req_origin == trip_dest and req_dest == trip_origin:
            score += Decimal("70")
            is_backhaul = True
            notes.append("Обратный рейс (backhaul)")
        else:
            return Decimal("0"), False, None

        if trip.free_capacity_kg >= request.weight_kg:
            score += Decimal("15")
        else:
            return Decimal("0"), is_backhaul, "Недостаточная грузоподъёмность"

        if request.pickup_date_from <= trip.departure_date:
            score += Decimal("5")

        if trip.is_return_leg and is_backhaul:
            score += Decimal("10")
            notes.append("Приоритет обратного рейса")

        return min(score, Decimal("100")), is_backhaul, "; ".join(notes) if notes else None

    @classmethod
    async def suggest_for_request(
        cls,
        session: AsyncSession,
        cargo_request_id: int,
    ) -> list[Match]:
        result = await session.execute(
            select(CargoRequest).where(CargoRequest.id == cargo_request_id)
        )
        request = result.scalar_one_or_none()
        if not request or request.status not in (
            CargoRequestStatus.PUBLISHED,
            CargoRequestStatus.DRAFT,
        ):
            return []

        trips_result = await session.execute(
            select(Trip).where(Trip.status == TripStatus.AVAILABLE)
        )
        trips = trips_result.scalars().all()

        created: list[Match] = []
        for trip in trips:
            score, is_backhaul, comment = cls.compute_score(request, trip)
            if score <= 0:
                continue
            match = Match(
                cargo_request_id=request.id,
                trip_id=trip.id,
                score=score,
                is_backhaul=is_backhaul,
                status=MatchStatus.SUGGESTED,
                comment=comment,
            )
            session.add(match)
            created.append(match)

        await session.flush()
        return created
