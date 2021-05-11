import core.models
import folders


class User(BaseModels):
    pass


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
