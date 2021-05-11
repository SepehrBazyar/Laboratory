from core.models import *
from typing import Optional


class User(BaseModels):
    first_name: str
    last_name: str
    phone: str
    email = Optional[str]
    password: str
    extra_information: dict

    # TODO : username
    def __init__(self, first_name, last_name, phone, password, email=None, **extra_information):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.password = password
        self.extra_information = extra_information

    def __repr__(self):
        return f"""<[first name:{self.first_name}, 
        last name:{self.last_name}]>"""


class Patient(User):
    pass


class Doctor(User):
    pass


class Operator(User):
    pass


class Sampler(User):
    pass


class Admin(User):  # Developer
    pass


class Manager(User):
    pass
