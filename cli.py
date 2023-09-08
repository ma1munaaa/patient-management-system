import click
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from models import Patient, Doctor, Appointment, Prescription, Base
from database import engine

Session = sessionmaker(bind=engine)

@click.group()
def cli():
    pass

@cli.command()
def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")
# Commands for patient management

@cli.command()
def create_patient():
    session = Session()
    name = input("Patient Name: ")
    birth_date = input("Date of Birth (YYYY-MM-DD): ")
    contact_details = input("Contact Details: ")
    address = input("Address: ")

    try:
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD format.")
        return

    patient = Patient(name=name, birth_date=birth_date, contact_details=contact_details, address=address)
    session.add(patient)
    session.commit()
    print("Patient created successfully.")

@cli.command()
def list_patients():
    session = Session()
    patients = session.query(Patient).all()
    for patient in patients:
        print(f"ID: {patient.id}, Name: {patient.name}, Birth Date: {patient.birth_date}, Contact: {patient.contact_details}, Address: {patient.address}")

# Commands for doctor management

@cli.command()
def create_doctor():
    session = Session()
    name = input("Doctor Name: ")
    specialization = input("Specialization: ")
    contact_details = input("Contact Details: ")

    doctor = Doctor(name=name, specialization=specialization, contact_details=contact_details)
    session.add(doctor)
    session.commit()
    print("Doctor created successfully.")

@cli.command()
def list_doctors():
    session = Session()
    doctors = session.query(Doctor).all()
    for doctor in doctors:
        print(f"ID: {doctor.id}, Name: {doctor.name}, Specialization: {doctor.specialization}, Contact: {doctor.contact_details}")

# Commands for appointment management

@cli.command()
def create_appointment():
    session = Session()
    patient_id = int(input("Patient ID: "))
    doctor_id = int(input("Doctor ID: "))
    date = input("Appointment Date (YYYY-MM-DD): ")
    status = input("Status: ")
    remarks = input("Remarks: ")

    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD format.")
        return

    appointment = Appointment(patient_id=patient_id, doctor_id=doctor_id, date=date, status=status, remarks=remarks)
    session.add(appointment)
    session.commit()
    print("Appointment created successfully.")

@cli.command()
def list_appointments():
    session = Session()
    appointments = session.query(Appointment).all()
    for appointment in appointments:
        print(f"ID: {appointment.id}, Patient: {appointment.patient.name}, Doctor: {appointment.doctor.name}, Date: {appointment.date}, Status: {appointment.status}, Remarks: {appointment.remarks}")

# Commands for prescription management

@cli.command()
def create_prescription():
    session = Session()
    patient_id = int(input("Patient ID: "))
    doctor_id = int(input("Doctor ID: "))
    prescription_date = input("Prescription Date (YYYY-MM-DD): ")
    medications = input("Medications: ")
    dosage = input("Dosage: ")
    instructions = input("Instructions: ")

    try:
        prescription_date = datetime.strptime(prescription_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD format.")
        return

    prescription = Prescription(patient_id=patient_id, doctor_id=doctor_id, prescription_date=prescription_date, medications=medications, dosage=dosage, instructions=instructions)
    session.add(prescription)
    session.commit()
    print("Prescription created successfully.")

@cli.command()
def list_prescriptions():
    session = Session()
    prescriptions = session.query(Prescription).all()
    for prescription in prescriptions:
        print(f"ID: {prescription.id}, Patient: {prescription.patient.name}, Doctor: {prescription.doctor.name}, Prescription Date: {prescription.prescription_date}, Medications: {prescription.medications}, Dosage: {prescription.dosage}, Instructions: {prescription.instructions}")

