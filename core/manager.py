import dill

from abc import ABC, abstractmethod


class BaseManager(ABC):
    @abstractmethod
    def create(self): pass

    @abstractmethod
    def read(self): pass

    @abstractmethod
    def update(self): pass

    @abstractmethod
    def delete(self): pass


class FileManager(BaseManager):
    def __init__(self, model) -> None:
        self.file = model.__name__ + 's.dill'
        try:
            with open(f".\\{self.file}", 'x') as fl:  # save to self directory?
                pass
        except:
            pass

    def create(self, ID, instance) -> bool:
        if not self.read(ID):
            with open(f".\\{self.file}", 'ab') as fl:
                fl.write(f"{str(ID)} ".encode())
                fl.write(dill.dumps(instance))
                fl.write(b'\n')
            return True
        return False

    def read(self, ID=None, attribute=None):
        with open(f".\\{self.file}", 'rb') as fl:
            models = dill.load(fl)
        if not ID:
            return models
        if ID in models:
            return getattr(models[ID], ID, models[ID])
        else:
            return False

    def update(self, ID, new_value, attribut=None):
        instance = self.read(ID)

    def delete(self, ID):
        pass


class DatabaseManager(BaseManager):
    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
