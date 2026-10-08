from fastapi import APIRouter, HTTPException, status
from sqlalchemy import select

from app.dependencies import DbSession
from app.models.cargo_request import CargoRequest
from app.schemas.cargo_request import (
    CargoRequestCreate,
    CargoRequestRead,
    CargoRequestUpdate,
)

router = APIRouter()


@router.get("", response_model=list[CargoRequestRead])
async def list_cargo_requests(db: DbSession) -> list[CargoRequest]:
    result = await db.execute(select(CargoRequest).order_by(CargoRequest.created_at.desc()))
    return list(result.scalars().all())


@router.post("", response_model=CargoRequestRead, status_code=status.HTTP_201_CREATED)
async def create_cargo_request(payload: CargoRequestCreate, db: DbSession) -> CargoRequest:
    # TODO: привязка к текущему пользователю после JWT-dependency
    item = CargoRequest(**payload.model_dump(), owner_id=1)
    db.add(item)
    await db.flush()
    await db.refresh(item)
    return item


@router.get("/{request_id}", response_model=CargoRequestRead)
async def get_cargo_request(request_id: int, db: DbSession) -> CargoRequest:
    result = await db.execute(select(CargoRequest).where(CargoRequest.id == request_id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Заявка не найдена")
    return item


@router.patch("/{request_id}", response_model=CargoRequestRead)
async def update_cargo_request(
    request_id: int,
    payload: CargoRequestUpdate,
    db: DbSession,
) -> CargoRequest:
    result = await db.execute(select(CargoRequest).where(CargoRequest.id == request_id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Заявка не найдена")

    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(item, key, value)

    await db.flush()
    await db.refresh(item)
    return item
