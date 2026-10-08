from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Vehicle(Base):
    """Транспортное средство перевозчика."""

    __tablename__ = "vehicles"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    carrier_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    plate_number: Mapped[str] = mapped_column(String(16), unique=True)
    vehicle_type: Mapped[str] = mapped_column(String(64))
    capacity_kg: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    capacity_m3: Mapped[Decimal | None] = mapped_column(Numeric(12, 2), nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True)

    carrier: Mapped["User"] = relationship(back_populates="vehicles")
    trips: Mapped[list["Trip"]] = relationship(back_populates="vehicle")


from app.models.trip import Trip  # noqa: E402
from app.models.user import User  # noqa: E402
