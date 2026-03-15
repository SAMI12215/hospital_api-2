from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# الاتصال بقاعدة البيانات
conn = sqlite3.connect("hospital.db", check_same_thread=False)
cursor = conn.cursor()

# إنشاء جدول المرضى إذا لم يكن موجود
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
