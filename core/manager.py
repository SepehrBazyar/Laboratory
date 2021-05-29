import json
# import psycopg2
import logging

from abc import ABC, abstractmethod
from .exceptions import *


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)-10s - %(message)s')


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
    Managed JSON Files to CRUD Data of Models.
    """

    def __init__(self, name: str, path: str) -> None:
        self.file, self.path = name + 's.json', path
        try:
            with open(f".\\{self.path}\\{self.file}", 'x') as fl:
                json.dump({}, fl, indent=4)
            logging.info(f"{__name__}: {self.file} File Created in {path} Directory.")
        except FileExistsError:
            logging.warning(f"{__name__}: {self.file} File Existed in {path} Directory.")
        logging.debug(f"{__name__}: File Manager Successfully.")

    def create(self, ID, instance) -> bool:
        """
        Create a New Value in the File By ID for Key and Self for Value.
        """
        models = self.read()
        if ID not in models:
            models[ID] = instance.__dict__
            with open(f".\\{self.path}\\{self.file}", 'w') as fl:
                json.dump(models, fl, indent=4)
            logging.info(f"{__name__}: {ID} Object Created And Save to File.")
            return True
        logging.error(f"{__name__}: {ID} Object Existed in the File.")
        return False
        raise UserExistError(f"{__name__}: {ID} Object Existed in the File.")

    def read(self, ID=None, attribute: str = None):
        """
        Read Data File and Return All of them or one Item by ID and Attribute.
        """
        with open(f".\\{self.path}\\{self.file}", 'r') as fl:
            models = json.load(fl)
        if not ID:
            logging.debug(f"{__name__}: Read And Pass All of the Objects.")
            return models
        if ID in models:
            logging.debug(f"{__name__}: Read And Pass Attribute(s) {ID} Object.")
            return models[ID].get(attribute, models[ID])
        logging.error(f"{__name__}: {ID} Not Existed Can't Read Anything.")
        return False
        raise UserNotFoundError(f"{__name__}: {ID} Not Existed Can't Read Anything.")

    def update(self, ID, attribute: str, new_value) -> bool:
        """
        Update Information of a Model in the Data File with the ID.
        """
        models = self.read()
        if ID in models:
            models[ID].update({attribute: new_value})
            with open(f".\\{self.path}\\{self.file}", 'w') as fl:
                json.dump(models, fl, indent=4)
            logging.info(f"{__name__}: {ID}.{attribute} Updated to {new_value}.")
            return True
        logging.error(f"{__name__}: {ID} Not Existed Can't Change Nothing.")
        return False
        raise UserNotFoundError(f"{__name__}: {ID} Not Existed Can't Change Nothing.")

    def delete(self, ID) -> bool:
        """
        Delete a Model by the ID from the Data File.
        """
        models = self.read()
        if ID in models:
            models.pop(ID)
            with open(f".\\{self.path}\\{self.file}", 'w') as fl:
                json.dump(models, fl, indent=4)
            logging.warning(f"{__name__}: {ID} Object Deleted Successfully.")
            return True
        logging.error(f"{__name__}: {ID} Object Not Existed in the File.")
        return False
        raise UserNotFoundError(f"{__name__}: {ID} Object Not Existed in the File.")


class DatabaseManager(BaseManager):
    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
