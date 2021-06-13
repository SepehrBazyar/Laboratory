import json
import re
from typing import Optional, Literal, Dict, Union
import time
import user.models as models


def inputer(txt: str, type_str: str, is_optional: str = False,
            check_valid: Literal["email", "phone_number"] = None,
            **extra_data):
    try:
        res = exec(f"{type_str}(input('{txt}'))")
    except TypeError:
        print(f"your input must be {type_str}\ntry again:")
        return inputer(txt, type_str, is_optional, check_valid, **extra_data)
    if not is_optional and res == "":
        print("its not optional and you should enter sth:")
        return inputer(txt, type_str, is_optional, check_valid, **extra_data)
    if check_valid == "email" or check_valid == "phone_number":

        print(f"isvalid = CheckValid.{check_valid}('{extra_data[f'{check_valid}']}')")
        isvalid = eval(f"CheckValid.{check_valid}('{extra_data[f'{check_valid}']}')")
        print(f"is valid is {isvalid}")
        if not isvalid:
            print(f"its not valid {check_valid}")
            return inputer(txt, type_str, is_optional, check_valid, **extra_data)
    return res


class CheckValid:
    __email_regex = r"^([\w\.\_\-]+)[@]([\w\.\_\-]*\w)[.]([A-Za-z]{2,3})$"
    __phone_number_regex = "^(0)?([]|-|[()]){0}09[0|1|2|3|4]([()]){0}(?:[0-9]([ ]|-|[()]){0,0}){8}$"

    @classmethod
    def email(cls, email: str) -> bool:
        return re.search(cls.__email_regex, email)

    @classmethod
    def phone_number(cls, phone_number: str):
        return re.search(cls.__phone_number_regex, phone_number)

    @classmethod
    def username(cls, username: str):
        pass


def login_authorization():
    print("login_authorization")
    time.sleep(1)
    # todo : this should return the type of user. Type of user is str type like "patient"
    return True


def retrieve_user(data: tuple) -> models.User:
    # extracting extra_info from json file
    extra_info = json.loads(json.dumps(data[7]))
    user = models.Patient(first_name=data[0].strip(), last_name=data[1].strip(), national_code=data[2].strip(),
                          phone=data[3].strip(), email=data[4], password=data[5].strip(), **extra_info)
    return user
