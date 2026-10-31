
from pydantic import BaseModel


class AppointmentCreate(BaseModel):

    patient_id: int

    doctor_id: int

    appointment_date: str

    appointment_time: str

    reason: str


class AppointmentResponse(BaseModel):

    id: int

    patient_id: int

    doctor_id: int

    appointment_date: str

    appointment_time: str

    reason: str

    status: str

    model_config = {
        "from_attributes": True
    }
