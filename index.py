# Parent Class : Person
class Person:
    def __init__(self, first_name, last_name, age, gender, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.phone = phone


# Patient
class Patient(Person):
    def __init__(self, first_name , last_name, age, gender, phone, patient_id):
        super().__init__(first_name, last_name, age, gender, phone)
        self.patient_id = patient_id
        self.medical_history_notes = []
        self.previous_visit_summaries = []

# Doctor
class Doctor(Person):
    def __init__(self, first_name , last_name, age, gender, phone, doctor_id, specialization, experience):
        super().__init__(first_name, last_name, age, gender, phone)
        self.doctor_id = doctor_id
        self.specialization = specialization
        self.experience = experience
        self.schedule = []


# Appointment
class Appointment:
    def __init__(self, appointment_id, patient, doctor, date, time, purpose):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
        self.purpose = purpose


# Medical Record
class MedicalRecord:
    def __init__(self, record_id, patient, doctor, diagnosis, visit_date, prescribed_medicine):
        self.record_id = record_id
        self.patient = patient
        self.doctor = doctor
        self.diagnosis = diagnosis
        self.visit_date = visit_date
        self.prescribed_medicines = prescribed_medicine

# Medicine
class Medicine:
    def __init__(self, name, unit_price, stock):
        self.name = name
        self.unit_price = unit_price
        self.stock = stock


# Pharmacy order
class PharmacyOrder:
    def __init__(self, order_id, patient, medicines_with_qty):
        self.order_id = order_id
        self.patient = patient
        self.medicines_with_qty = medicines_with_qty
        self.total_cost = 0

    def calculate_total(self):
        total = 0
        for medicine, qty in self.medicines_with_qty.items():
            if qty <= medicine.stock:
                total += medicine.unit_price * qty
                medicine.stock -= qty
        self.total_cost = total


# Bill
class Bill:
    def __init__(self, bill_id, patient, consultation, procedures, medicines):
        self.bill_id = bill_id
        self.patient = patient
        self.consultation = consultation
        self.procedures = procedures
        self.medicines = medicines
        self.total = consultation + procedures + medicines
        self.is_paid = False

    def mark_paid(self):
        self.is_paid = True


p = Patient('Hammad' , 'Khalid' , 13 , 'Male' , '0319000000', 1)
d = Doctor("Sumbal", "Naz", 18, "Female", "0300-2222222", 101, "Cardiology", 12)

appt = Appointment(1, p, d, "25-11-2025", "10:30", "Checkup")

record = MedicalRecord(1, p, d, "Fever", "25-11-2025", ["Panadol"])

med = Medicine("Panadol", 20, 50)
order = PharmacyOrder(1, p, {med: 2})
order.calculate_total()

bill = Bill(1, p, consultation=500, procedures=0, medicines=order.total_cost)
bill.mark_paid()

print("Patient:", p.first_name)
print("Doctor:", d.first_name)
print("Appointment:", appt.date, appt.time)
print("Diagnosis:", record.diagnosis)
print("Order Total:", order.total_cost)
print("Bill Paid:", bill.is_paid)