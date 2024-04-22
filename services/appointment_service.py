from schemas.appointment import AppointmentCreate, Appointment
from schemas.patient import BaseModel
from schemas.doctor import BaseModel
from services.doctor_service import DoctorService
from services.patient_service import PatientService
import uuid

class AppointmentService:
    def __init__(self, patient_service: PatientService, doctor_service: DoctorService):
        self.appointments = []
        self.patient_service = patient_service
        self.doctor_service = doctor_service

    def book_appointment(self, appointment: AppointmentCreate) -> Appointment:
        appointment_id = str(uuid.uuid4())
        patient = next((p for p in self.patient_service.patients if p.id == appointment.patient_id), None)
        doctor = next((d for d in self.doctor_service.doctors if d.id == appointment.doctor_id), None)

        if not patient or not doctor or not doctor.is_available:
            raise ValueError("Invalid patient, doctor, or doctor is not available")

        new_appointment = Appointment(id=appointment_id, **appointment.dict())
        self.appointments.append(new_appointment)
        doctor.is_available = False
        return new_appointment