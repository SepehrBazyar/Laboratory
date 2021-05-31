from user import models
from Lab.models import CV19
from time import sleep

Patient_list = []
Tests = []


def cv19_view():
    print("Enter your profile : ")
    first_name = input("First Name : ")
    last_name = input("Last Name : ")
    phone = input("Phone : ")
    email = input("Email(Optional) : ")

    patient = models.Patient(first_name, last_name, phone, email)
    Patient_list.append(patient)

    print("Your profile saved !")
    print("Testing patient ", end="")

    [sleep(1) or print(".", end="") for i in range(3)]

    cv19 = CV19(patient)

    print("Done ! ")

    Tests.append(cv19)
    print("Estimated result time : ", cv19.estimate_time)


def result():
    pass


def update_test():
    pass


def repr_all_test():
    pass


def manage_test():
    pass
