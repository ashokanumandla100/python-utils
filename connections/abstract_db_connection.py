from abc import ABC, abstractmethod


class DBConnection(ABC):

    @abstractmethod
    def connect(self, conn_str):
        pass

    @abstractmethod
    def execute(self, query):
        pass

    @abstractmethod
    def executemany(self, prep_stmt, chunk):
        pass

    @abstractmethod
    def get_marker(self, length):
        pass

    @abstractmethod
    def executeproc(self, proc_name, **args):
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
