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
    """
    Managed Files to CRUD Data of Models.
    """

    def __init__(self, name, path) -> None:
        self.file, self.path = name + 's.dill', path
        with open(f".\\{self.path}\\{self.file}", 'x') as fl:  # TODO : save to self directory
            dill.dump({}, fl)

    def create(self, ID, instance) -> bool:
        """
        Create a New Value in the File By ID for Key and Self for Value.
        """
        models = self.read()
        if ID not in models:
            models[ID] = instance
            with open(f".\\{self.path}\\{self.file}", 'wb') as fl:
                dill.dump(models, fl)
            return True
        return False

    def read(self, ID=None, attribute: str = None):
        """
        Read Data File and Return All of them or one Item by ID and Attribute.
        """
        with open(f".\\{self.path}\\{self.file}", 'rb') as fl:
            models = dill.load(fl)
        if not ID:
            return models
        if ID in models:
            return getattr(models[ID], attribute, models[ID])
        return False

    def update(self, ID, attribute: str, new_value) -> bool:
        """
        Update Information of a Model in the Data File with the ID.
        """
        models = self.read()
        if ID in models:
            setattr(models[ID], attribute, new_value)
            with open(f".\\{self.path}\\{self.file}", 'wb') as fl:
                dill.dump(models, fl)
            return True
        return False

    def delete(self, ID) -> bool:
        """
        Delete a Model by the ID from the Data File.
        """
        models = self.read()
        if ID in models:
            models.pop(ID)
            with open(f".\\{self.path}\\{self.file}", 'wb') as fl:
                dill.dump(models, fl)
            return True
        return False


class DatabaseManager(BaseManager):
    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
