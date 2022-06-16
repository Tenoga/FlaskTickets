import pymysql
def mysqlConnect():
    conn = pymysql.Connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = '',
        db = 'coltrans')
    return conn