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
        models = self.read()
        if ID not in models:
            models[ID] = instance
            with open(f".\\{self.file}", 'wb') as fl:
                dill.dump(models, fl)
            return True
        return False

    def read(self, ID=None, attribute: str = None):
        with open(f".\\{self.file}", 'rb') as fl:
            models = dill.load(fl)
        if not ID:
            return models
        if ID in models:
            return getattr(models[ID], attribute, models[ID])
        else:
            return False

    def update(self, ID, attribute: str, new_value) -> bool:
        models = self.read()
        if ID in models:
            setattr(models[ID], attribute, new_value)
            with open(f".\\{self.file}", 'wb') as fl:
                dill.dump(models, fl)
            return True
        else:
            return False

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
