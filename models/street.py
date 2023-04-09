from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from db.database import Base


class Street(Base):
    __tablename__ = 'streets'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    city_id = Column(Integer, ForeignKey('cities.id'))

    city = relationship('City', back_populates='streets')

    __table_args__ = (
        UniqueConstraint('name', 'city_id', name='unique_city_street'),
    )