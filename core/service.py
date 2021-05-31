import os

from user.models import Admin
import logging


def initialize_setup():
    admin = Admin()
    username = admin.username
    password = admin.password
    with open(os.getcwd() + "/data/admin.info", "wt") as info_file:
        print(f"username: {username}, pass={password}", file=info_file)
    logging.info("admin.info is created")
