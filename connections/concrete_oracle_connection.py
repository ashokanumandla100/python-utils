from .abstract_db_connection import DBConnection
import cx_Oracle


class OracleConnection(DBConnection):

    def __init__(self):
        self._cur = None
        self._conn = None

    def connect(self, conn_str):
        host, port, service, user, pwd = conn_str.split(';')
        dsn = cx_Oracle.makedsn(
            host=host,
            port=port,
            service_name=service
        )
        self._conn = cx_Oracle.connect(
            user=user,
            password=pwd,
            dsn=dsn,
            encoding="UTF-8"
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

