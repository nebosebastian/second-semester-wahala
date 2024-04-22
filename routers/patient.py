from fastapi import APIRouter, Depends
from schemas.patient import PatientCreate, Patient
from services.patient_service import PatientService
from typing import List

patient_router = APIRouter()


@patient_router.post("/", response_model=Patient)
def create_patient(patient: PatientCreate, patient_service: PatientService = Depends(PatientService)):
    return patient_service.create_patient(patient)

@patient_router.get("/{patient_id}/appointments", response_model=List)
def get_patient_appointments(patient_id: str, patient_service: PatientService = Depends(PatientService)):
    return patient_service.get_patient_appointments(patient_id)

