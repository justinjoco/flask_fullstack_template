from abc import ABC, abstractmethod

class Cache(ABC):

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_id(self, id):
        pass

    @abstractmethod
    def save(self, object):
        pass

    @abstractmethod
    def save_all(self, objects):
        pass

    @abstractmethod
    def delete_by_id(self, id):
        pass

    @abstractmethod
    def health_check(self):
        pass

