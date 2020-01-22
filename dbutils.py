import cx_Oracle
import pyodbc
import ibm_db_dbi


class OracleConnection:
    """context manager for oracle connection"""

    def __init__(self, host, port, service, user, password):
        self.host = host
        self.port = port
        self.service = service
        self.user = user
        self.password = password
        self.conn = None

    def __enter__(self):
        self.dsn = cx_Oracle.makedsn(
            self.host, self.port, service_name=self.service)
        self.conn = cx_Oracle.connect(
            user=self.user, password=self.password, dsn=self.dsn, encoding="UTF-8")
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()


class OracleCursor:
    """context manager for oracle cursor"""

    def __init__(self, conn):
        self.conn = conn
        self.cur = None

    def __enter__(self):
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()


class SQLServerConnection:
    """context manager for sqlserver connection"""

    def __init__(self, host, port, db, user, password):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.password = password
        self.conn = None

    def __enter__(self):
        self.conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.host},{self.port};DATABASE={self.db};UID={self.user};PWD={self.password}")
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()


class SQLServerCursor:
    """context manager for sqlserver cursor"""

    def __init__(self, conn):
        self.conn = conn
        self.cur = None

    def __enter__(self):
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()


class DB2Connection:
    """context manager for db2 connection"""

    def __init__(self, host, port, db, user, password):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.password = password
        self.conn = None

    def __enter__(self):
        self.conn = ibm_db_dbi.connect(
            f"HOSTNAME={self.host};PORT={self.port};PROTOCOL=TCPIP;DATABASE={self.db};UID={self.user};PWD={self.password}")
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()


class DB2Cursor:
    """context manager for db2 cursor"""

    def __init__(self, conn):
        self.conn = conn
        self.cur = None

    def __enter__(self):
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()


if __name__ == "__main__":
    ora_conn = OracleConnection(host='hostname', port='1521', service='servicename',
                                user='username', password='password')

    with ora_conn as conn:
        with OracleCursor(conn) as cur:
            cur.execute('SELECT COUNT(*) from TABLE')
            rs = cur.fetchall()

    print(rs)

    ss_conn = SQLServerConnection(host='hostname', port='1433', db='dbname',
                                  user='username', password='password')

    with ss_conn as conn:
        with SQLServerCursor(conn) as cur:
            cur.execute('SELECT COUNT(*) from TABLE')
            rs = cur.fetchall()

    print(rs)

    db2_conn = DB2Connection(host='hostname', port='50000', db='dbname',
                             user='username', password='password')

    with db2_conn as conn:
        with DB2Cursor(conn) as cur:
            cur.execute('SELECT COUNT(*) from TABLE')
            rs = cur.fetchall()

    print(rs)
