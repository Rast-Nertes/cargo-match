from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from app.models.cargo_request import CargoRequestStatus


class CargoRequestBase(BaseModel):
    origin_city: str = Field(min_length=1, max_length=128)
    origin_address: str | None = None
    destination_city: str = Field(min_length=1, max_length=128)
    destination_address: str | None = None
    cargo_description: str = Field(min_length=1)
    weight_kg: Decimal = Field(gt=0)
    volume_m3: Decimal | None = Field(default=None, gt=0)
    pickup_date_from: date
    pickup_date_to: date | None = None
    delivery_date: date | None = None
    price: Decimal | None = Field(default=None, ge=0)
    currency: str = "RUB"


class CargoRequestCreate(CargoRequestBase):
    pass


class CargoRequestUpdate(BaseModel):
    origin_city: str | None = None
    destination_city: str | None = None
    cargo_description: str | None = None
    weight_kg: Decimal | None = Field(default=None, gt=0)
    status: CargoRequestStatus | None = None
    price: Decimal | None = Field(default=None, ge=0)


class CargoRequestRead(CargoRequestBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    owner_id: int
    status: CargoRequestStatus
    created_at: datetime
    updated_at: datetime
