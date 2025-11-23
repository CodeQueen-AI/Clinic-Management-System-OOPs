# **🏥 Clinic Management System – Python OOP**

## **⭐ Purpose**

Ye program ek **hospital management system** ka basic simulation hai jo **patients, doctors, appointments, medical records, pharmacy orders, aur billing** ko manage karta hai




## **⭐Features**

1. **Patient Management**

   * Store patient details: name, age, gender, phone
   * Track medical history and previous visit summaries

2. **Doctor Management**

   * Store doctor details: name, specialization, experience
   * Manage doctor schedule

3. **Appointments**

   * Schedule appointments between patients and doctors
   * Track date, time, and purpose of visit

4. **Medical Records**

   * Store diagnosis, visit date, prescribed medicines

5. **Pharmacy Orders**

   * Place medicine orders for patients
   * Track stock and calculate total cost automatically

6. **Billing System**

   * Generate bills for consultation, procedures, and medicines
   * Mark bills as paid


## **⭐ How It Works**

* **Classes** are used to model real-world entities: `Patient`, `Doctor`, `Appointment`, `MedicalRecord`, `Medicine`, `PharmacyOrder`, `Bill`
* **Relationships**:

  * Appointment links **Patient** and **Doctor**
  * MedicalRecord links **Patient** and **Doctor** with diagnosis and medicines
  * PharmacyOrder tracks medicines and calculates total
  * Bill tracks payment for services and medicines



## **⭐ Key Benefits**

* Organizes **hospital data efficiently**
* Automates **billing and pharmacy calculations**
* Easy to **extend**: add new features like reports, notifications, or insurance handling
