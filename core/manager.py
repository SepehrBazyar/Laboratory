import json

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
        self.file, self.path = name + 's.json', path
        try:
            with open(f".\\{self.path}\\{self.file}", 'x') as fl:
                json.dump({}, fl, indent=4)
        except:
            pass

    def create(self, ID, instance) -> bool:
        """
        Create a New Value in the File By ID for Key and Self for Value.
        """
        models = self.read()
        if ID not in models:
            models[ID] = instance.__dict__
            with open(f".\\{self.path}\\{self.file}", 'w') as fl:
                json.dump(models, fl, indent=4)
            return True
        return False

    def read(self, ID=None, attribute: str = None):
        """
        Read Data File and Return All of them or one Item by ID and Attribute.
        """
        with open(f".\\{self.path}\\{self.file}", 'r') as fl:
            models = json.load(fl)
        if not ID:
            return models
        if ID in models:
            return models[ID].get(attribute, models[ID])
        return False

    def update(self, ID, attribute: str, new_value) -> bool:
        """
        Update Information of a Model in the Data File with the ID.
        """
        models = self.read()
        if ID in models:
            models[ID].update({attribute: new_value})
            with open(f".\\{self.path}\\{self.file}", 'w') as fl:
                json.dump(models, fl, indent=4)
            return True
        return False

    def delete(self, ID) -> bool:
        """
        Delete a Model by the ID from the Data File.
        """
        models = self.read()
        if ID in models:
            models.pop(ID)
            with open(f".\\{self.path}\\{self.file}", 'w') as fl:
                json.dump(models, fl, indent=4)
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
