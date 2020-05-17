from .abstract_db_connection import DBConnection
import pyodbc


class SqlServerConnection(DBConnection):

    def __init__(self):
        self._conn = None
        self._cur = None

    def connect(self, conn_str):
        host, port, db, user, pwd = conn_str.split(';')
        self._conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={host},{port};"
            f"DATABASE={db};"
            f"UID={user};"
            f"PWD={pwd};"
        )
        self._cur = self._conn.cursor()

    def execute(self, query):
        self._cur.execute(query)

    def fetchmany(self, n):
        return self._cur.fetchmany(n)

    def fetchall(self):
        return self._cur.fetchall()

    def disconnect(self):
        if self._cur:
            self._cur.close()
        if self._conn:
            self._conn.close()

