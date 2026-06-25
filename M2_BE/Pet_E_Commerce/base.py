from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData


class Base(DeclarativeBase):
    metadata = MetaData(schema="pet_e_commerce")