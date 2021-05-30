from datetime import datetime, timedelta

from core.models import BaseModels
from user.models import Patient
from Lab.exceptions import *


class Basetest(BaseModels):
    patients = Patient
    estimate_time, result_time, create_time = datetime

    def __init__(self, patient) -> None:
        self.patient = patient
        self.__result = None
        self.create_time, self.estimate_time = datetime

    def set_result(self, result):
        self.result_time = datetime.now()
        self.__result = result
