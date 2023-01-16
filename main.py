from fastapi import FastAPI
from car_license_plates.routers import car_plates
from Token.routers import token

app = FastAPI()

app.include_router(
    car_plates,
    prefix="/plate",
    tags=["plate"],
    responses={418: {"description": "plate"}},
)


app.include_router(
    token,
    prefix="/token",
    tags=["token"],
    responses={418: {"description": "token"}},
)
