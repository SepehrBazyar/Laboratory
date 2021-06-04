import os.path
from hashlib import sha256

from core.models import *
from core.manager import *
from typing import Optional, Literal
import secrets
import string


class User(BaseModels):
    first_name: str
    last_name: str
    phone: str
    email: str = None
    _password: str
    extra_information: dict

    # TODO : username
    def __init__(self, first_name, last_name, national_code, phone, type_of_users_id,password, email=None, **extra_information):
        self.first_name = first_name
        self.last_name = last_name
        self.national_code = national_code
        self.phone = phone
        self.email = email
        self.type_of_users_id = type_of_users_id
        self._password = password
        # self.extra_information = extra_information
        # self.extra_information = extra_information

    # TODO: ask about pass private from mr.tehrani
    def get_password(self):
        return self._password

    def __repr__(self):
        return f"""
                <first name:{self.first_name}, 
                 last  name:{self.last_name}>
                """


class Patient(User):
    gender: Literal["male", "female"]
    age: int
    blood_type: Optional[Literal["O", "A", "B", "AB"]]
    _FILE = FileManager("Patient")
    patients = list(_FILE.read().values())

    def __init__(self, first_name, last_name, national_code, phone, type_of_users_id, password, gender, age, blood_type,
                 email=None, **extra_information):
        super().__init__(first_name, last_name, national_code, phone, type_of_users_id, password, email, **extra_information)
        self.gender = gender
        self.age = age
        self.blood_type = blood_type
        # todo: we should change id for creating file from phone to national_code
        self.__class__._FILE.create(self.national_code, self)
        self.__class__.patients = list(self.__class__._FILE.read().values())


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


class Admin:  # Site Admin

    # declare as a class attr, because if we need more than one admin, we are able to save in this file
    _admin_FILE = FileManager("Admin")

    def __init__(self):
        if "admin" in self._admin_FILE.read().keys():
            with open(os.getcwd() + "\\data\\Admins.json", 'r') as fl:
                admins = json.load(fl)
            admin_dict = admins["admin"]
            self.username = admin_dict["username"]
            self._password = admin_dict["_password"]

        else:
            self.username = "admin"
            self._password = self.__pass_generator()
            # self.__admin_password = sha256(self.__password.encode()).hexdigest()
            # admin has not national_code, so we pass his/her username
            self.__class__._admin_FILE.create(self.username, self)

    @staticmethod
    def __pass_generator():
        alphabet = string.ascii_letters + string.digits
        password_local = ''.join(secrets.choice(alphabet) for i in range(10))  # for a 10-character password
        return password_local

    @property
    def password(self):
        return self._password

# todo : postponed
# class Manager(User):
#     educational_degree: str
#
#     def __init__(self, first_name, last_name, phone, password, educational_degree, email=None, **extra_information):
#         super().__init__(first_name, last_name, phone, password, email, **extra_information)
#         self.educational_degree = educational_degree
#
#     def __repr__(self):
#         return super().__repr__() + f"educational_degree:{self.educational_degree}"

# TODO : postponed
# class Sampler(User):
#     pass
