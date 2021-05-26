from core.models import *
from core.manager import *
from typing import Optional, Literal


class User(BaseModels):
    first_name: str
    last_name: str
    phone: str
    email = Optional[str]
    __password: str
    extra_information: dict

    # TODO : username
    def __init__(self, first_name, last_name, phone, email=None, **extra_information):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        # self.__password = password
        self.extra_information = extra_information

    # TODO: ask about pass private from mr.tehrani
    def get_password(self):
        return self.__password

    def __repr__(self):
        return f"""
<[first name:{self.first_name}, 
last name:{self.last_name}]>
"""


class Patient(User):
    @staticmethod
    def __loading(information: dict) -> list:
        users, result = list(information.values()), []
        for user in users:
            inform = list(user.values())
            result.append(Patient(*inform[0:3], *inform[5:8], inform[3]))

    gender: Literal["male", "female"]
    age: int
    blood_type: Optional[Literal["O", "A", "B", "AB"]]
    _FILE = FileManager("Patient", __name__.split('.')[0])
    patients = __loading(_FILE.read())

    def __init__(self, first_name, last_name, phone, gender, age, blood_type, email=None, **extra_information):
        super().__init__(first_name, last_name, phone, email, **extra_information)
        self.gender = gender
        self.age = age
        self.blood_type = blood_type
        self._FILE.create(self.phone, self)
        self.patients = self._FILE.read()


class Doctor(User):
    # sampler and check the tests
    expertise: str

    def __init__(self, first_name, last_name, phone, password, expertise, email=None, **extra_information):
        super().__init__(first_name, last_name, phone, password, email, **extra_information)
        self.expertise = expertise

    def __repr__(self):
        return super().__repr__() + f"expertise:{self.expertise}"


class Operator(User):
    licence: str

    def __init__(self, first_name, last_name, phone, password, licence, email=None, **extra_information):
        super().__init__(first_name, last_name, phone, password, email, **extra_information)
        self.licence = licence

    def __repr__(self):
        return super().__repr__() + f"licence:{self.licence}"


# TODO : postponed
# class Sampler(User):
#     pass


# TODO : postponed
# class Admin(User):  # Developer
#     pass


class Manager(User):
    pass
