from .abstract_db_connection import DBConnection
import ibm_db


class DB2Connection(DBConnection):

    def __init__(self):
        self._connected = False
        self._conn = None
        self._stmt = None
        self._rs = None

    def connect(self, conn_str):
        host, port, db, user, pwd = conn_str.split(';')
        _conn_str = (
            f"PROTOCOL=TCPIP;"
            f"HOSTNAME={host};"
            f"PORT={port};"
            f"DATABASE={db};"
            f"UID={user};"
            f"PWD={pwd};"
        )
        self._conn = ibm_db.connect(_conn_str, "", "")
        self._connected = True

    def execute(self, query):
        self._stmt = ibm_db.exec_immediate(self._conn, query)
        self._rs = None

    def gen_result(self):
        row = ibm_db.fetch_tuple(self._stmt)
        while row:
            yield row
            row = ibm_db.fetch_tuple(self._stmt)

    def fetchmany(self, n):
        if not self._rs:
            self._rs = self.gen_result()
        out = []
        for i in range(n):
            try:
                out.append(next(self._rs))
            except StopIteration as e:
                pass
        return out

    def fetchall(self):
        return [_ for _ in self.gen_result()]

    def disconnect(self):
        if self._connected:
            ibm_db.close(self._conn)

