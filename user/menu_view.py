from time import sleep
from core.utility import *
from hashlib import sha256
from getpass import getpass
import user.models as models
from lab.models import CV19
import core.manager as core_manager
from core.utility import retrieve_user as retrieve_user

db_manger = core_manager.DatabaseManager()


def register():
    first_name = input("enter your first name:")
    last_name = input("enter your last name:")
    national_code = input("enter your national code:")
    phone = input("enter your phone number:")
    email = input("enter your email(optional):") or None
    password = input("enter your password:")
    user_type = input("enter your type:")
    user_type_id = db_manger.get_id('user_type', type=user_type)
    extra_data = (db_manger.read('user_type', row_id=user_type_id))[0][1]
    extra_data = json.dumps(extra_data)
    extra_data_dict = json.loads(extra_data)
    for key, value in extra_data_dict.items():
        value = input(f"enter your {key}:")
        extra_data_dict.update({f"{key}": f"{value}"})
    if user_type == 'patient':
        user = models.Patient(first_name=first_name, last_name=last_name, national_code=national_code, phone=phone,
                              password=password, email=email, **extra_data_dict)
    elif user_type == 'doctor':
        user = models.Doctor(first_name=first_name, last_name=last_name, national_code=national_code, phone=phone,
                             password=password, email=email, **extra_data_dict)
    elif user_type == 'operator':
        user = models.Operator(first_name=first_name, last_name=last_name, national_code=national_code, phone=phone,
                               password=password, email=email, **extra_data_dict)
    db_manger.create(table="users", model=user)
    print("Congrats. Your Account Is Created")


def login():
    user_name = input("enter your username (national_code):")
    password = input("enter your password:")
    password_hashed = sha256(password.encode()).hexdigest()
    check_res = db_manger.check_record('users', national_code=user_name, password=password_hashed)
    user = retrieve_user(check_res[0])
    return user if check_res else False


def repr_all_patients():
    users = db_manger.read_all("users")
    for user in users:
        print(user)


def repr_all_doctors():
    pass


def repr_all_operators():
    pass


def register_doctor():
    pass


def register_operator():
    pass


def manage_users():
    pass
