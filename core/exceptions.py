class AllException(Exception):
    pass


class UserExistError(AllException):
    """
    User Already Exist in the Database.
    """


class UserNotFoundError(AllException):
    """
    User Not Found in the Database.
    """


class Static:
    pass
