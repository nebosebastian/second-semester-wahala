from pydantic import BaseModel
from typing import Optional

class DoctorCreate(BaseModel):
    name: str
    specialization: str
    phone: str

class Doctor(DoctorCreate):
    id: str
    is_available: bool = True
