from fastapi import FastAPI

from routers.doctor import doctor_router
from routers.patient import patient_router
from routers.appointment import appointment_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to our Medical API"}


#register router
app.include_router(doctor_router, prefix="/doctors", tags=["Doctors"])
app.include_router(patient_router, prefix="/patient", tags=["Patients"])
app.include_router(appointment_router, prefix="/appointment", tags=["Appointments"])

 