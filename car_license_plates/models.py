from sqlalchemy import Column, Integer, String
from sgl_app.db import Base


class CarPlates(Base):
    __tablename__ = 'car_plates'

    id_car_plates = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    plate = Column(String(10), autoincrement=False, nullable=False)
