from abc import ABC, abstractmethod


class DBConnection(ABC):

    @abstractmethod
    def connect(self, conn_str):
        pass

    @abstractmethod
    def execute(self, query):
        pass

    @abstractmethod
    def fetchmany(self, n):
        pass

    @abstractmethod
    def fetchall(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass
