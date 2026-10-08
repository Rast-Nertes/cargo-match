from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from app.models.trip import TripStatus


class TripBase(BaseModel):
    origin_city: str = Field(min_length=1, max_length=128)
    destination_city: str = Field(min_length=1, max_length=128)
    departure_date: date
    arrival_date: date | None = None
    vehicle_type: str = Field(min_length=1, max_length=64)
    capacity_kg: Decimal = Field(gt=0)
    capacity_m3: Decimal | None = Field(default=None, gt=0)
    free_capacity_kg: Decimal = Field(gt=0)
    is_return_leg: bool = False
    notes: str | None = None


class TripCreate(TripBase):
    pass


class TripUpdate(BaseModel):
    departure_date: date | None = None
    free_capacity_kg: Decimal | None = Field(default=None, gt=0)
    status: TripStatus | None = None
    notes: str | None = None


class TripRead(TripBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    carrier_id: int
    status: TripStatus
    created_at: datetime
