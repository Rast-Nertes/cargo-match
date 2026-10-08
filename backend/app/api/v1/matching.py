from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from app.dependencies import DbSession
from app.models.match import Match
from app.schemas.match import MatchRead
from app.services.matching_service import MatchingService

router = APIRouter()


@router.get("/cargo-request/{request_id}", response_model=list[MatchRead])
async def list_matches_for_request(request_id: int, db: DbSession) -> list[Match]:
    result = await db.execute(
        select(Match)
        .where(Match.cargo_request_id == request_id)
        .order_by(Match.score.desc())
    )
    return list(result.scalars().all())


@router.post(
    "/cargo-request/{request_id}/suggest",
    response_model=list[MatchRead],
)
async def suggest_matches(request_id: int, db: DbSession) -> list[Match]:
    matches = await MatchingService.suggest_for_request(db, request_id)
    if not matches:
        existing = await db.execute(
            select(Match.cargo_request_id).where(Match.cargo_request_id == request_id).limit(1)
        )
        if not existing.scalar_one_or_none():
            raise HTTPException(
                status_code=404,
                detail="Заявка не найдена или нет подходящих рейсов",
            )
    return matches
