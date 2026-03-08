from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

patients = []

class Patient(BaseModel):
    id: int
    name: str
    condition: str

@app.get("/")
def home():
    return {"message": "Hospital System Running"}

@app.get("/patients")
def get_patients():
    return patients

@app.post("/patients")
def add_patient(patient: Patient):
    patients.append(patient)
    return {"message": "Patient added"}

@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int):
    global patients
    patients = [p for p in patients if p.id != patient_id]
    return {"message": "Patient deleted"}