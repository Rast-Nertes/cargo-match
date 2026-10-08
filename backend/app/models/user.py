import enum
from datetime import datetime

from sqlalchemy import DateTime, Enum, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class UserRole(str, enum.Enum):
    SHIPPER = "shipper"
    CARRIER = "carrier"
    ADMIN = "admin"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    full_name: Mapped[str] = mapped_column(String(255))
    company_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    phone: Mapped[str | None] = mapped_column(String(32), nullable=True)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.SHIPPER)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    cargo_requests: Mapped[list["CargoRequest"]] = relationship(
        back_populates="owner", foreign_keys="CargoRequest.owner_id"
    )
    trips: Mapped[list["Trip"]] = relationship(back_populates="carrier")


from app.models.cargo_request import CargoRequest  # noqa: E402
from app.models.trip import Trip  # noqa: E402
