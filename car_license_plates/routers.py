from fastapi import APIRouter
from . import utils
from . import schema
from fastapi import Depends
from sqlalchemy.orm import Session
from sgl_app.db import get_db, create_bd
from .models import CarPlates

from Token import authentication

car_plates = APIRouter()


@car_plates.get("/generate")
async def generate_plates(amount: int = None, auth: str = Depends(authentication.get_current_user)):
    """ Функция генерирует автомобильные номера """
    amount = 1 if amount in [None, 0] else amount
    dict_numbers = utils.creating_numbers(amount)
    return utils.response_user(success=True, numbers=dict_numbers)


@car_plates.get("/get")
async def all_numbers(id: int = None, auth: str = Depends(authentication.get_current_user),
                      db: Session = Depends(get_db)):
    """ Функция возвращает  автомобильные номера из базы данных по id """
    if id < 1 or id is None:
        return utils.response_user(success=False, numbers="Введите корректный id")
    id_number = db.query(CarPlates).get(id)
    if id_number:
        return utils.response_user(success=True, numbers=schema.GetNumbers(**id_number.__dict__).dict())
    return utils.response_user(success=True, numbers=f"Записи с id = {id} нет.")


@car_plates.post("/add")
async def save_plates(plate: schema.SaveNumbers,
                      auth: str = Depends(authentication.get_current_user),
                      db: Session = Depends(get_db)):
    """ Функция сохранения в базу данных автомобильного номера """
    if utils.number_control(plate.plate):
        plate_dict = plate.dict()
        obj = CarPlates(**plate_dict)
        create_bd(db, obj)
        return utils.response_user(success=True, numbers=f"'{plate.plate}' номер успешно сохранен")
    return utils.response_user(success=True, numbers=f"'{plate.plate}' формат номера не соответствует стандарту!")
