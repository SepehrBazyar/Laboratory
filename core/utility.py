import re
from typing import Optional, Literal, Dict, Union


def get_input(txt: str, type_str: str, is_optional: str = False,
              check_valid: Literal["email", "phone_number"] = None,
              **extra_data):
    try:
        res = exec(f"{type_str}(input('{txt}'))")
    except TypeError:
        print(f"your input must be {type_str}\ntry again:")
        return get_input(txt, type_str, is_optional, check_valid, **extra_data)
    if not is_optional and res == "":
        print("its not optional and you should enter sth:")
        return get_input(txt, type_str, is_optional, check_valid, **extra_data)
    if check_valid == "email" or check_valid == "phone_number":

        print(f"isvalid = CheckValid.{check_valid}('{extra_data[f'{check_valid}']}')")
        isvalid = eval(f"CheckValid.{check_valid}('{extra_data[f'{check_valid}']}')")
        print(f"is valid is {isvalid}")
        if not isvalid:
            print(f"its not valid {check_valid}")
            return get_input(txt, type_str, is_optional, check_valid, **extra_data)
    return res


class CheckValid:
    __email_regex = "^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"
    __phone_number_regex = "^(0)?([]|-|[()]){0}09[0|1|2|3|4]([()]){0}(?:[0-9]([ ]|-|[()]){0,0}){8}$"

    @classmethod
    def email(cls, email: str) -> bool:
        return True if re.search(cls.__email_regex, email) else False

    @classmethod
    def phone_number(cls, phone_number: str):
        return True if re.search(cls.__phone_number_regex, phone_number) else False


print(CheckValid.email("rasoolahad1997@gmail.com"))
