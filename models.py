from sqlalchemy import Column, Integer, String, Date, Float
from database import Base

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"

    id = Column(Integer, primary_key=True, index=True)
    wheel_number = Column(String, unique=True, index=True)
    diameter = Column(Float)
    width = Column(Float)
    material = Column(String)
    inspection_date = Column(Date)

class BogieChecksheet(Base):
    __tablename__ = "bogie_checksheet"

    id = Column(Integer, primary_key=True, index=True)
    bogie_number = Column(String, unique=True, index=True)
    inspector_name = Column(String)
    status = Column(String)
    checked_on = Column(Date)
