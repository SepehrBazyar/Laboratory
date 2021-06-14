import json
from datetime import datetime, timedelta
from typing import List

from user import models
from lab.models import CV19
from time import sleep
from core.manager import DatabaseManager

db_manager = DatabaseManager()

Patient_list = []
Tests = []


def register_test(test_name, patient):
    request_date = datetime.today().strftime('%Y-%m-%d')
    result_date = (datetime.today() + timedelta(days=7)).strftime('%Y-%m-%d')
    user_id = db_manager.get_id('users', national_code=patient.national_code)
    test_info_id = db_manager.get_id('test_info', test_name=test_name)
    cv19_test = CV19(request_date=request_date, result_date=result_date, user_id=user_id, test_info_id=test_info_id)
    db_manager.create(table="tests", model=cv19_test)
    print("Done ! ")
    print("Estimated result time : ", cv19_test.result_date)



def result(test_id):
    test = db_manager.read(table='tests', row_id=test_id)
    res = test[0][2]
    res = json.dumps(res)
    res = json.loads(res)
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
