from connections.concrete_oracle_connection import OracleConnection
from connections.concrete_sqlserver_connection import SqlServerConnection
from connections.concrete_db2_connection import DB2Connection

def main():
    ora_conn = OracleConnection()
    ora_conn.connect("<host>;1521;<service>;<username>;<password>")
    ora_conn.execute("SELECT COUNT(1) FROM ANSWER_OPTION")

    result = ora_conn.fetchall()
    print(result)
    ora_conn.disconnect()

    ss_conn = SqlServerConnection()
    ss_conn.connect("<host>;1433;<service>;<username>;<password>")
    ss_conn.execute("SELECT COUNT(1) FROM ANSWER_OPTION")

    result = ss_conn.fetchall()
    print(result)

    ss_conn.disconnect()

    db2_conn = DB2Connection()
    db2_conn.connect("<host>;50000;<service>;<username>;<password>")
    db2_conn.execute("SELECT COUNT(1) FROM BL.ANSWER_OPTION")

    result = db2_conn.fetchall()
    print(result)

    db2_conn.disconnect()


if __name__ == "__main__":
    main()