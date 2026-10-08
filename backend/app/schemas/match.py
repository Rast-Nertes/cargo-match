from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict

from app.models.match import MatchStatus


class MatchRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    cargo_request_id: int
    trip_id: int
    score: Decimal
    is_backhaul: bool
    status: MatchStatus
    comment: str | None
    created_at: datetime
