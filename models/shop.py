from sqlalchemy import Column, ForeignKey, Integer, String, Time, UniqueConstraint
from sqlalchemy.orm import relationship

from db.database import Base


class Shop(Base):
    __tablename__ = 'shops'


    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    city_id = Column(Integer, ForeignKey('cities.id'))
    street_id = Column(Integer, ForeignKey('streets.id'))
    house = Column(Integer)
    opening_time = Column(Time)
    closing_time = Column(Time)

    city = relationship('City')
    street = relationship('Street')

    __table_args__ = (
        UniqueConstraint('name', 'city_id', 'street_id', name='unique_city_street_shop'),
    )