
from sqlalchemy import Column, Integer, String
from database import Base


class Appointment(Base):

    __tablename__ = "appointments"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    patient_id = Column(Integer, nullable=False)

    doctor_id = Column(Integer, nullable=False)

    appointment_date = Column(String(20))

    appointment_time = Column(String(20))

    reason = Column(String(200))

    status = Column(
        String(30),
        default="CONFIRMED"
    )
