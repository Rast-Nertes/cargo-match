import enum
from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import Date, DateTime, Enum, ForeignKey, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class TripStatus(str, enum.Enum):
    PLANNED = "planned"
    AVAILABLE = "available"
    PARTIALLY_LOADED = "partially_loaded"
    IN_TRANSIT = "in_transit"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Trip(Base):
    """Рейс перевозчика (в т.ч. обратный рейс)."""

    __tablename__ = "trips"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    carrier_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    vehicle_id: Mapped[int | None] = mapped_column(
        ForeignKey("vehicles.id"), nullable=True, index=True
    )

    origin_city: Mapped[str] = mapped_column(String(128), index=True)
    destination_city: Mapped[str] = mapped_column(String(128), index=True)

    departure_date: Mapped[date] = mapped_column(Date, index=True)
    arrival_date: Mapped[date | None] = mapped_column(Date, nullable=True)

    vehicle_type: Mapped[str] = mapped_column(String(64))
    capacity_kg: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    capacity_m3: Mapped[Decimal | None] = mapped_column(Numeric(12, 2), nullable=True)
    free_capacity_kg: Mapped[Decimal] = mapped_column(Numeric(12, 2))

    is_return_leg: Mapped[bool] = mapped_column(default=False, index=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    status: Mapped[TripStatus] = mapped_column(
        Enum(TripStatus), default=TripStatus.AVAILABLE, index=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    carrier: Mapped["User"] = relationship(back_populates="trips")
    vehicle: Mapped["Vehicle | None"] = relationship(back_populates="trips")
    matches: Mapped[list["Match"]] = relationship(back_populates="trip")


from app.models.match import Match  # noqa: E402
from app.models.user import User  # noqa: E402
from app.models.vehicle import Vehicle  # noqa: E402
