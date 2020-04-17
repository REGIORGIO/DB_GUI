import cx_Oracle


def getDBconnection(username, password):
    ip = 'localhost'
    port = 1521
    SID = 'xe'
    dsn_tns = cx_Oracle.makedsn(ip, port, SID)
    # print(dsn_tns)

    try:
        con = cx_Oracle.connect(username, password, dsn_tns, encoding="UTF-8")
        print('Succesfull connection')
        return con
    except cx_Oracle.Error as error:
        print(error)


def shutDownConnection(con):
    con.close()
    print('Connection closed')


con = getDBconnection('C##GEORGY', 'georgy')
curs = con.cursor()
curs.execute("select * from projects")
for row in curs:
    print(row)

