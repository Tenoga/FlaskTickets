from DB import mysqlConnect


# -------------- Funcion para editar un pasajero en la BD---------------------- #
def editarBuses(tipo, placa, compañia, capacidad):
    conn = mysqlConnect()
    with conn.cursor() as cursor:
        sql = "update bus set tipo= %s, placa= %s, compañia = %s, capacidad= %s where id = %s;"
        cursor.execute(sql, (tipo, placa, compañia, capacidad, id))
        conn.commit()
        conn.close()

# -------------- Funcion para consultar todos los valores de pasajeros en la BD---------------------- #
def consultarBuses():
    conn = mysqlConnect()
    bus = []
    with conn.cursor() as cursor:
        sql = "select * from bus"
        cursor.execute(sql)
        bus = cursor.fetchall()
        conn.close()
    return bus



# -------------- Funcion para Borrar pasajero---------------------- #
def borrarBus(id):
    conn = mysqlConnect()
    with conn.cursor() as cursor:
        sql = "delete from bus where id = %s"
        cursor.execute(sql, (id))
        conn.commit()
        conn.close()
    