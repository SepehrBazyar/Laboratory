import json
from datetime import datetime, timedelta

from core.models import BaseModels
from user.models import Patient
from lab.exceptions import *


class Basetest(BaseModels):
    patients: Patient
    estimate_time: datetime
    result_time: datetime
    create_time: datetime

    def __init__(self, patient) -> None:
        self.patient = patient
        self.__result = None
        self.create_time, self.estimate_time = datetime

    def set_result(self, result):
        self.result_time = datetime.now()
        self.__result = result


class CV19(Basetest):

    def has_cv19(self):
        if not hasattr(self, '__result'):
            raise Exception
        return bool(self.__result)


class TestInfo:
    def __init__(self, test_name, price, **test_info_extra_data):
        self.test_name = test_name
        self.price = price
        self.extra_data = json.dumps(test_info_extra_data)
