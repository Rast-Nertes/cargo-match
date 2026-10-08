import enum
from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import Date, DateTime, Enum, ForeignKey, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class CargoRequestStatus(str, enum.Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    MATCHED = "matched"
    IN_TRANSIT = "in_transit"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class CargoRequest(Base):
    """Заявка на грузоперевозку."""

    __tablename__ = "cargo_requests"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)

    origin_city: Mapped[str] = mapped_column(String(128), index=True)
    origin_address: Mapped[str | None] = mapped_column(String(512), nullable=True)
    destination_city: Mapped[str] = mapped_column(String(128), index=True)
    destination_address: Mapped[str | None] = mapped_column(String(512), nullable=True)

    cargo_description: Mapped[str] = mapped_column(Text)
    weight_kg: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    volume_m3: Mapped[Decimal | None] = mapped_column(Numeric(12, 2), nullable=True)

    pickup_date_from: Mapped[date] = mapped_column(Date)
    pickup_date_to: Mapped[date | None] = mapped_column(Date, nullable=True)
    delivery_date: Mapped[date | None] = mapped_column(Date, nullable=True)

    price: Mapped[Decimal | None] = mapped_column(Numeric(14, 2), nullable=True)
    currency: Mapped[str] = mapped_column(String(3), default="RUB")

    status: Mapped[CargoRequestStatus] = mapped_column(
        Enum(CargoRequestStatus), default=CargoRequestStatus.DRAFT, index=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    owner: Mapped["User"] = relationship(back_populates="cargo_requests")
    matches: Mapped[list["Match"]] = relationship(back_populates="cargo_request")


from app.models.match import Match  # noqa: E402
from app.models.user import User  # noqa: E402
