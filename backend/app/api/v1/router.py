from fastapi import APIRouter

from app.api.v1 import auth, cargo_requests, health, matching, trips

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(cargo_requests.router, prefix="/cargo-requests", tags=["cargo-requests"])
api_router.include_router(trips.router, prefix="/trips", tags=["trips"])
api_router.include_router(matching.router, prefix="/matching", tags=["matching"])
