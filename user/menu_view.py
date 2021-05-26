import user.models as models


def register():
    # user_type =
    first_name = input("enter your name:")
    last_name = input("enter your last name:")
    phone = input("enter your phone number:")
    email = input("enter your email(optional):")
    gender = input("enter your gender(male or female):")
    age = int(input("enter your  age:"))
    blood_type = input("enter your blood type(A,B,AB or O) :")
    # __password = input("enter your last name:")
    models.Patient(first_name, last_name, phone, gender, age, blood_type, email)
    print("**new user created**")


def repr_all_users():
    patients = models.Patient.patients

    for i in range(len(patients)):
        print(f"{i + 1}- ", patients[i])
