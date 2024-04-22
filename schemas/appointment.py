from pydantic import BaseModel
from typing import Optional

class AppointmentCreate(BaseModel):
    patient_id: str
    doctor_id: str
    date: str

class Appointment(BaseModel):
    id: str
    


