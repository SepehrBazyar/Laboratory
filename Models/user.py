from abc import ABC,abstractclassmethod

class User(ABC):
    pass

class Patient(User):
    pass

class Doctor(User):
    pass

class Operator(User):
    pass

class Sampler(User):
    pass

class Admin(User):#Developer
    pass

class Guest(User):
    pass

class Manager(User):
    pass