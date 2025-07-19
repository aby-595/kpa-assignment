from pydantic import BaseModel

class WheelSpecCreate(BaseModel):
    wheel_number: str
    diameter: float
    width: float
    material: str
    inspection_date: str

class BogieCheckCreate(BaseModel):
    bogie_number: str
    inspector_name: str
    status: str
    checked_on: str
