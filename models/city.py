
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)

    streets = relationship('Street', back_populates='city', cascade="all,delete")