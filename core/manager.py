import json
from psycopg2 import connect
from psycopg2._psycopg import connection, cursor
import logging
from contextlib import contextmanager
from abc import ABC, abstractmethod
import dbconfig
from .exceptions import *
from core.models import BaseModels

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)-10s - %(message)s')


class BaseManager(ABC):

    @abstractmethod
    def create(self, table, model): pass

    @abstractmethod
    def read(self, table): pass

    @abstractmethod
    def update(self, table, **kwargs): pass

    @abstractmethod
    def delete(self, table, row_id): pass


class FileManager(BaseManager):
    """
    Managed JSON Files to CRUD Data of Models.
    """

    def __init__(self, name: str) -> None:
        self.file, self.path = name + 's.json', 'data'
        try:
            with open(f".\\{self.path}\\{self.file}", 'x') as fl:
                json.dump({}, fl, indent=4)
            logging.info(f"{__name__}: {self.file} File Created in {self.path} Directory.")
        except FileExistsError:
            logging.warning(f"{__name__}: {self.file} File Existed in {self.path} Directory.")
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

    def create(self, table, model):
        attrs: dict = model.to_dict()
        dict_values = tuple(attrs.values())
        # todo for tests %s %s is different
        query = f"INSERT INTO {table} VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        self.send_query(query, dict_values)

    def read(self, table):
        query = f"SELECT * FROM {table}"
        with self.access_database() as lab_cursor:
            lab_cursor.execute(query)
            return lab_cursor.fetchall()

    def update(self, table, **kwargs):
        """kwargs should include id of a row and one or more column=amount for updating
            Example: row_id=1, first_name=reza, last_name=gholami"""
        set_string = ""
        condition_string_key = list(kwargs.keys())[0]
        condition_string_value = kwargs[condition_string_key]
        condition_string = f"{condition_string_key}='{condition_string_value}'"
        kwargs.pop(condition_string_key)
        for key, value in kwargs.items():
            set_string += f"{key}='{value}', "
        query = f"UPDATE {table} SET {set_string[:-2]} where {condition_string}"
        self.send_query(query)

    def delete(self, table, row_id):
        query = f"DELETE FROM {table} where id={row_id}"
        self.send_query(query)

    def get_id(self, table, **kwargs):
        """kwargs should include table name and one column=amount for searching
        Example: users, national-code=11111"""
        column = list(kwargs.keys())[0]
        value = kwargs[column]
        condition = f"{table}.{column}='{value}'"
        query = f"SELECT {table}.id from {table} where {condition};"
        with self.access_database() as lab_cursor:
            lab_cursor.execute(query)
            return lab_cursor.fetchone()[0]

    def check_record(self, table, **kwargs):
        """kwargs should include table name and one or more column=amount for checking
                Example: users, national-code=11111, password='12345'"""
        condition_string = ''
        for key, value in kwargs.items():
            condition_string += f"{key}='{value}' and "
        query = f"SELECT * from {table} where {condition_string[:-5]};"
        with self.access_database() as lab_cursor:
            lab_cursor.execute(query)
            return lab_cursor.fetchall()

    def send_query(self, query, data=None):
        with self.access_database() as lab_cursor:
            lab_cursor.execute(query, data)

    @contextmanager
    def access_database(self):
        conn: connection = connect(dbconfig.config)
        curs: cursor = conn.cursor()
        yield curs
        curs.close()
        conn.commit()
        conn.close()

    def normalizer(self):
        pass
