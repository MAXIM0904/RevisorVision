from pydantic import BaseModel


class GenerateNumbers(BaseModel):
    numbers: str


class ListGenerateNumbers(BaseModel):
    success: bool
    numbers: list | str | dict

    class Config:
        orm_mode = True


class SaveNumbers(BaseModel):
    plate: str


class GetNumbers(SaveNumbers):
    id_car_plates: int

    class Config:
        orm_mode = True