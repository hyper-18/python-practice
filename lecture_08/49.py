class Patient:
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.doctor = None

    def display_details(self):
        print("Patient ID:", self.patient_id)
        print("Patient Name:", self.name)
        print("Age:", self.age)


class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def display_details(self):
        print("Doctor Name:", self.name)
        print("Specialization:", self.specialization)


class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []

    def register_patient(self, patient):
        self.patients.append(patient)
        print(patient.name, "registered successfully.")

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print(doctor.name, "added successfully.")

    def assign_doctor(self, patient_id, doctor_name):
        patient = None
        doctor = None

        for p in self.patients:
            if p.patient_id == patient_id:
                patient = p
                break

        for d in self.doctors:
            if d.name == doctor_name:
                doctor = d
                break

        if patient is None:
            print("Patient not found.")
        elif doctor is None:
            print("Doctor not found.")
        else:
            patient.doctor = doctor
            print(doctor.name, "assigned to", patient.name)

    def display_records(self):
        print("\n===== HOSPITAL RECORDS =====")

        for patient in self.patients:
            print("\nPatient Details:")
            patient.display_details()

            if patient.doctor:
                print("Assigned Doctor:", patient.doctor.name)
                print("Specialization:", patient.doctor.specialization)
            else:
                print("Assigned Doctor: Not assigned")


# Creating hospital
hospital = Hospital("City Hospital")

# Creating patients
p1 = Patient(101, "Abhi", 18)
p2 = Patient(102, "Rahul", 20)

# Creating doctors
d1 = Doctor("Dr. Sharma", "Cardiologist")
d2 = Doctor("Dr. Patil", "Neurologist")

# Registering patients
hospital.register_patient(p1)
hospital.register_patient(p2)

# Adding doctors
hospital.add_doctor(d1)
hospital.add_doctor(d2)

# Assigning doctors
hospital.assign_doctor(101, "Dr. Sharma")
hospital.assign_doctor(102, "Dr. Patil")

# Displaying records
hospital.display_records()
