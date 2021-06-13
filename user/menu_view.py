from time import sleep
import user.models as models
from core.utility import *
from hashlib import sha256
from getpass import getpass
import user.models as models
from lab.models import CV19
import core.manager as core_manager
from core.utility import retrieve_user as retrieve_user

u_manger = core_manager.DatabaseManager()


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
    user_patient = models.Patient(first_name=first_name, last_name=last_name, national_code=national_code, phone=phone,
                                  password=password, email=email, gender=gender, age=age,
                                  blood_type=blood_type)
    u_manger.create(table="users", model=user_patient)
    print("Congrats. Your Account Is Created")

    # todo : we agreed to use national code ad username, so it should be considered in login


def login():
    user_name = input("enter your username (national_code):")
    password = input("enter your password:")
    check_res = u_manger.check_record('users', national_code=user_name, password=password)
    user = retrieve_user(check_res[0])
    return user if check_res else False


def repr_all_patients():
    users = u_manger.read("users")
    for user in users:
        print(user)


#     patients = models.Patient.patients
#     for i in range(len(patients)):
#         print(f"""
# {i + 1}-
# <first name:{patients[i]["first_name"]},
#  last  name:{patients[i]["last_name"]}>
# """)


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
