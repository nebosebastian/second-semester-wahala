from fastapi import APIRouter, Depends
from schemas.appointment import AppointmentCreate, Appointment
from services.appointment_service import AppointmentService

appointment_router = APIRouter()

@appointment_router.post("/", response_model=Appointment)
def book_appointment(appointment: AppointmentCreate, appointment_service: AppointmentService = Depends(AppointmentService)):
    return appointment_service.book_appointment(appointment)
