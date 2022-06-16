from DB import mysqlConnect


# -------------- Funcion para editar un pasajero en la BD---------------------- #
def editarRutas(origen, destino):
    conn = mysqlConnect()
    with conn.cursor() as cursor:
        sql = "update ruta set origen= %s, detino= %s where id = %s;"
        cursor.execute(sql, (origen, destino, id))
        conn.commit()
        conn.close()

# -------------- Funcion para consultar todos los valores de pasajeros en la BD---------------------- #
def consultarRutas():
    conn = mysqlConnect()
    bus = []
    with conn.cursor() as cursor:
        sql = "select * from ruta"
        cursor.execute(sql)
        bus = cursor.fetchall()
        conn.close()
    return bus



# -------------- Funcion para Borrar pasajero---------------------- #
def borrarRutas(id):
    conn = mysqlConnect()
    with conn.cursor() as cursor:
        sql = "delete from ruta where id = %s"
        cursor.execute(sql, (id))
        conn.commit()
        conn.close()


