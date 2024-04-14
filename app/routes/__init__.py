from fastapi import APIRouter

from .post import router_post

router = APIRouter(prefix="/api", tags=["VRB"])

router.include_router(router_post)
