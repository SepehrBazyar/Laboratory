from time import sleep
import user.models as models
from core.utility import *
from hashlib import sha256
from getpass import getpass
import user.models as models
from lab.models import CV19


def register():
    first_name = input("enter your first name:")
    last_name = input("enter your last name:")
    national_code = input("enter your national code:")
    phone = input("enter your phone number:")
    email = input("enter your email(optional):") or None
    # password = sha256(getpass(
    #     "enter your password:").encode()).hexdigest()  # Commented During Developing. This Needs To BE Run From Command propmt
    password = "1234"  # it is just for test
    gender = input("enter your gender(male or female):")
    age = int(input("enter your  age:"))
    blood_type = input("enter your blood type(A,B,AB or O) :")
    models.Patient(first_name, last_name, national_code, phone, email, password, gender, age, blood_type)
    print("Congrats. Your Account Is Created")

    # todo : we agreed to use national code ad username, so it should be considered in login


def repr_all_patients():
    patients = models.Patient.patients
    for i in range(len(patients)):
        print(f"""
{i + 1}-
<first name:{patients[i]["first_name"]}, 
 last  name:{patients[i]["last_name"]}>
""")


def repr_all_doctors():
    pass


def repr_all_operators():
    pass


def register_doctor():
    pass


def register_operator():
    pass


def manage_users():
    pass
