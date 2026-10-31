
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
from database import engine, get_db
from schemas import AppointmentCreate, AppointmentResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Hospital Appointment Service",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Appointment Service is running",
        "port": 8003
    }


@app.post(
    "/appointments",
    response_model=AppointmentResponse,
    status_code=201
)
def create_appointment(
    appointment: AppointmentCreate,
    db: Session = Depends(get_db)
):

    new_appointment = models.Appointment(
        **appointment.model_dump()
    )

    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)

    return new_appointment


@app.get("/appointments")
def get_appointments(
    db: Session = Depends(get_db)
):

    return db.query(models.Appointment).all()


@app.get("/appointments/{appointment_id}")
def get_appointment(
    appointment_id: int,
    db: Session = Depends(get_db)
):

    appointment = db.query(models.Appointment).filter(
        models.Appointment.id == appointment_id
    ).first()

    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    return appointment


@app.patch("/appointments/{appointment_id}/cancel")
def cancel_appointment(
    appointment_id: int,
    db: Session = Depends(get_db)
):

    appointment = db.query(models.Appointment).filter(
        models.Appointment.id == appointment_id
    ).first()

    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    appointment.status = "CANCELLED"

    db.commit()

    return {
        "message": "Appointment cancelled successfully",
        "appointment_id": appointment_id,
        "status": appointment.status
    }
