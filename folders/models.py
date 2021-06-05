import datetime


class Archive:
    def add(self):
        pass

    def delete(self):
        pass


class Lab:
    def result(self):
        pass

    def pending(self):
        pass

    def present(self):
        pass

    def cancel(self):
        pass


class Folder:
    def __init__(self):
        lab = Lab()

    @classmethod
    def add_to_archive(cls):
        pass
