from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from config import PASSWORD

SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{PASSWORD}@localhost/city_shops"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()