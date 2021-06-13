import re


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
