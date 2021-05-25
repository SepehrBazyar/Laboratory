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
        self.file = model.__name__ + '.dill'
        try:
            with open(f".\\{self.file}", 'x') as fl:
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

    def read(self, ID, attribute=None):
        with open(f".\\{self.file}", 'rb') as fl:
            flag = True
            while flag:
                model = fl.readline().strip().split()
                if not model:
                    break
                if model[0].decode() == str(ID):
                    flag = False
        if flag:
            return None
        instance = dill.loads(model[1])
        return getattr(instance, attribute, instance)

    def update(self, ID, new_value, attribut=None):
        pass

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
