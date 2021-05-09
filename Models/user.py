from abc import ABC,abstractclassmethod
import folders

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

class Manager(User):
    pass
