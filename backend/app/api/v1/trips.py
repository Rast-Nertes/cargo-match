from fastapi import APIRouter, HTTPException, status
from sqlalchemy import select

from app.dependencies import DbSession
from app.models.trip import Trip
from app.schemas.trip import TripCreate, TripRead, TripUpdate

router = APIRouter()


@router.get("", response_model=list[TripRead])
async def list_trips(db: DbSession) -> list[Trip]:
    result = await db.execute(select(Trip).order_by(Trip.departure_date.desc()))
    return list(result.scalars().all())


@router.post("", response_model=TripRead, status_code=status.HTTP_201_CREATED)
async def create_trip(payload: TripCreate, db: DbSession) -> Trip:
    item = Trip(**payload.model_dump(), carrier_id=1)
    db.add(item)
    await db.flush()
    await db.refresh(item)
    return item


@router.get("/{trip_id}", response_model=TripRead)
async def get_trip(trip_id: int, db: DbSession) -> Trip:
    result = await db.execute(select(Trip).where(Trip.id == trip_id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Рейс не найден")
    return item


@router.patch("/{trip_id}", response_model=TripRead)
async def update_trip(trip_id: int, payload: TripUpdate, db: DbSession) -> Trip:
    result = await db.execute(select(Trip).where(Trip.id == trip_id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Рейс не найден")

    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(item, key, value)

    await db.flush()
    await db.refresh(item)
    return item
