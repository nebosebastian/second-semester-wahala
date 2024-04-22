from schemas.doctor import DoctorCreate, Doctor
from schemas.appointment import Appointment
import uuid

class DoctorService:
    def _init_(self):
        self.doctors = []
        self.appointments = []

    def create_doctor(self, doctor: DoctorCreate) -> Doctor:
        doctor_id = str(uuid.uuid4())
        new_doctor = Doctor(id=doctor_id, **doctor.dict())
        self.doctors.append(new_doctor)
        return new_doctor

    def get_doctor_appointments(self, doctor_id: str) -> list[Appointment]:
        return [appointment for appointment in self.appointments if appointment.doctor_id == doctor_id]
