from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

conn = sqlite3.connect("hospital.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY,
    name TEXT,
    condition TEXT
)
""")

conn.commit()

class Patient(BaseModel):
    id: int
    name: str
    condition: str

@app.get("/")
def home():
    return {"message": "Hospital System Running"}

@app.get("/patients")
def get_patients():
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()
    return rows

@app.post("/patients")
def add_patient(patient: Patient):
    cursor.execute(
        "INSERT INTO patients (id,name,condition) VALUES (?,?,?)",
        (patient.id, patient.name, patient.condition)
    )
    conn.commit()
    return {"message": "Patient added"}

@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int):
    cursor.execute("DELETE FROM patients WHERE id=?", (patient_id,))
    conn.commit()
    return {"message": "Patient deleted"}
