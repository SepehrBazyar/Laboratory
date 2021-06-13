import json
from typing import List

from user import models
from lab.models import CV19
from time import sleep
from core.manager import DatabaseManager

db_manager = DatabaseManager()

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


def result(test_id):
    test = db_manager.read(table='tests', row_id=test_id)
    res = test[0][2]
    return res


def update_test_res(test_id, result: json):
    """
    result must be a json file
    """
    db_manager.update_json_content(table='tests', id=test_id, result=result)
    return "Test Is Updated"


def user_tests(user) -> List[tuple]:
    # it returns test.id, national_code, first_name, last_name, type, test_name, request_date, result_date
    tests = db_manager.read_user_tests(user)
    for i in range(len(tests)):
        tests[i] = list(map(lambda item: item.strip() if type(item) == str else item, tests[i]))
    return tests


def repr_all_test():
    pass


def manage_test():
    pass
