from sqlalchemy import Column, DateTime, Integer, String
from datetime import datetime
from app.database.tables.base import Base


class Services(Base):
    __tablename__ = "services"
    id = Column(Integer(), primary_key=True)
    uri = Column(String(200))
    created_on = Column(DateTime(), default=datetime.now())
    updated_on = Column(DateTime(), default=datetime.now(), onupdate=datetime.now())
