from fastapi import APIRouter, Depends
from schemas.doctor import DoctorCreate, Doctor
from services.doctor_service import DoctorService
from typing import List

doctor_router = APIRouter()

doctors = []

@doctor_router.post("/", response_model=Doctor)
def create_doctor(doctor: DoctorCreate, doctor_service: DoctorService = Depends(DoctorService)):
    return doctor_service.create_doctor(doctor)

@doctor_router.get("?{doctor_id}/appointments",response_model=list)
def get_doctor_appointments(doctor_id: str, doctor_service: DoctorService = Depends(DoctorService)):
    return doctor_service.get_doctor_appointments(doctor_id)