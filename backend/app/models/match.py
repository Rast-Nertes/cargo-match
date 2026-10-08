import enum
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, Enum, ForeignKey, Numeric, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class MatchStatus(str, enum.Enum):
    SUGGESTED = "suggested"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    EXPIRED = "expired"


class Match(Base):
    """Результат автоматического сопоставления заявки с рейсом."""

    __tablename__ = "matches"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cargo_request_id: Mapped[int] = mapped_column(
        ForeignKey("cargo_requests.id"), index=True
    )
    trip_id: Mapped[int] = mapped_column(ForeignKey("trips.id"), index=True)

    score: Mapped[Decimal] = mapped_column(Numeric(5, 2))
    is_backhaul: Mapped[bool] = mapped_column(default=False)
    status: Mapped[MatchStatus] = mapped_column(
        Enum(MatchStatus), default=MatchStatus.SUGGESTED, index=True
    )
    comment: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    cargo_request: Mapped["CargoRequest"] = relationship(back_populates="matches")
    trip: Mapped["Trip"] = relationship(back_populates="matches")


from app.models.cargo_request import CargoRequest  # noqa: E402
from app.models.trip import Trip  # noqa: E402
