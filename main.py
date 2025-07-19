from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, WheelSpecification, BogieChecksheet
import schemas

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "🚀 KPA API is running"}

# Create Wheel Specification with duplicate check
@app.post("/wheel-spec")
def create_wheel_spec(spec: schemas.WheelSpecCreate, db: Session = Depends(get_db)):
    existing = db.query(WheelSpecification).filter_by(wheel_number=spec.wheel_number).first()
    if existing:
        return {"error": f"Wheel number '{spec.wheel_number}' already exists."}
    wheel = WheelSpecification(**spec.dict())
    db.add(wheel)
    db.commit()
    db.refresh(wheel)
    return wheel

# Get all Wheel Specifications
@app.get("/wheel-spec")
def get_all_wheel_specs(db: Session = Depends(get_db)):
    return db.query(WheelSpecification).all()

# Create Bogie Checksheet with duplicate check
@app.post("/bogie-check")
def create_bogie_checksheet(data: schemas.BogieCheckCreate, db: Session = Depends(get_db)):
    existing = db.query(BogieChecksheet).filter_by(bogie_number=data.bogie_number).first()
    if existing:
        return {"error": f"Bogie number '{data.bogie_number}' already exists."}
    bogie = BogieChecksheet(**data.dict())
    db.add(bogie)
    db.commit()
    db.refresh(bogie)
    return bogie

# Get all Bogie Checksheets
@app.get("/bogie-check")
def get_all_bogie_checksheets(db: Session = Depends(get_db)):
    return db.query(BogieChecksheet).all()
