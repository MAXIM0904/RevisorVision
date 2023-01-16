from fastapi import APIRouter
from . import schema
from . import authentication


token = APIRouter()


@token.get("/generate", response_model=schema.Token)
async def generate_token():
    """ Функция генерации токена """
    access_token = authentication.create_access_token(data={"sub": '123456789'})
    return {"token": access_token}
