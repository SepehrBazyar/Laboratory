import json
from datetime import datetime, timedelta

from core.models import BaseModels
from user.models import Patient
from lab.exceptions import *


class Basetest(BaseModels):
    request_date: datetime
    result_date: datetime
    result: json
    user_id: int
    test_info_id: int

    def __init__(self, request_date, result_date, user_id, test_info_id):
        self.request_date = request_date
        self.result_date = result_date
        self.result = json.dumps({})
        self.user_id = user_id
        self.test_info_id = test_info_id

    def get_result(self):
        return self.result


class CV19(Basetest):

    def __init__(self, request_date, result_date, user_id, test_info_id):
        super().__init__(request_date, result_date, user_id, test_info_id)


class TestInfo:
    def __init__(self, test_name, price, **test_info_extra_data):
        self.test_name = test_name
        self.price = price
        self.extra_data = json.dumps(test_info_extra_data)
