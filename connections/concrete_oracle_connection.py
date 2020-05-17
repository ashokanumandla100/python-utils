from .abstract_db_connection import DBConnection
import cx_Oracle


def output_type_handler(cursor, name, defaultType, size, precision, scale):
    if defaultType == cx_Oracle.CLOB:
        return cursor.var(cx_Oracle.LONG_STRING, arraysize=cursor.arraysize)

    if defaultType == cx_Oracle.BLOB:
        return cursor.var(cx_Oracle.LONG_BINARY, arraysize=cursor.arraysize)


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
        self._cur.outputtypehandler = output_type_handler

    def execute(self, query):
        self._cur.execute(query)

    def executemany(self, prep_stmt, chunk):
        self._cur.executemany(prep_stmt, chunk)

    def get_marker(self, length):
        return ", ".join([f':{i+1}' for i in range(length)])

    def executeproc(self, proc_name, **args):
        if len(args) > 0:
            self._cur.callproc(proc_name, list(args))
        else:
            self._cur.callproc(proc_name)

    def fetchmany(self, n):
        return self._cur.fetchmany(n)

    def fetchall(self):
        return self._cur.fetchall()

    def disconnect(self):
        if self._cur:
            self._cur.close()
        if self._conn:
            self._conn.close()

