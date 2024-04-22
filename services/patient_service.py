from schemas.patient import PatientCreate, Patient
import uuid

class PatientService:
    def _init_(self):
        self.patients = []

    def create_patient(self, patient: PatientCreate) -> Patient:
        patient_id = str(uuid.uuid4())
        new_patient = Patient(id=patient_id, **patient.dict())
        self.patients.append(new_patient)
        return new_patient

    def get_patient_appointments(self, patient_id: str) -> list:
        return [appointment for appointment in self.appointments if appointment.patient_id == patient_id]
