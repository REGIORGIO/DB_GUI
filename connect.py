import cx_Oracle


def getDBconnection(username, password):
    ip = 'localhost'
    port = 1521
    SID = 'xe'
    dsn_tns = cx_Oracle.makedsn(ip, port, SID)
    username = 'C##GEORGY'
    password = 'georgy'

    return cx_Oracle.connect(username, password, dsn_tns, encoding="UTF-8")


def shutDownConnection(con):
    con.commit()
    con.close()
    print('Connection closed')


if __name__ == '__main__':
    con = getDBconnection('C##GEORGY', 'georgy')
    curs = con.cursor()
    curs.execute("select * from projects")
    for row in curs:
        print(row)

