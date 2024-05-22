from sqlalchemy import Column, Integer, String, DateTime, Text

# from sqlalchemy.orm import declarative_base
from database import Base
from datetime import datetime
from sqlalchemy.orm import relationship, backref


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    age = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
