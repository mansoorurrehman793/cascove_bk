from fastapi import APIRouter

router = APIRouter()


@router.get("/auth/register", tags=["auth"])
async def register():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/auth/login", tags=["auth"])
async def login():
    return [{"username": "Rick"}, {"username": "Morty"}]
