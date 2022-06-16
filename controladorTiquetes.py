from DB import mysqlConnect

# -------------- Funcion para insertar un pasajero en la BD---------------------- #
def crearTiquetes(cantidad, fecha_viaje, hora_salida, id_bus, id_pasajero, id_ruta):
    conn = mysqlConnect()
    with conn.cursor() as cursor:
        sql = "insert into tiquetes (cantidad, fecha_viaje, hora_salida, id_bus, id_pasajero, id_ruta) Values(%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (cantidad, fecha_viaje, hora_salida, id_bus, id_pasajero, id_ruta))
        conn.commit()
        conn.close()

# -------------- Funcion para editar un tiquete en la BD---------------------- #
def editarTiquetes(cantidad, fecha_viaje, hora_salida, id_bus, id_pasajero, id_ruta, id):
    conn = mysqlConnect()
    with conn.cursor() as cursor:
        sql = "update tiquetes set cantidad= %s, fecha_viaje= %s, hora_salida = %s, id_bus= %s, id_pasajero= %s, id_ruta = %s where id = %s;"
        cursor.execute(sql, (cantidad, fecha_viaje, hora_salida, id_bus, id_pasajero, id_ruta, id))
        conn.commit()
        conn.close()

# -------------- Funcion para consultar todos los valores de pasajeros en la BD---------------------- #
# def consultarTiquetes():
#     conn = mysqlConnect()
#     tiquetes = []
#     with conn.cursor() as cursor:
#         sql = "select * from tiquetes"
#         cursor.execute(sql)
#         tiquetes = cursor.fetchall()
#         conn.close()
#     return tiquetes

def consultarTiquetes():
    try :
        conn = mysqlConnect()
        tiquetes = []
        with conn.cursor() as cursor:
            sql = """SELECT t.id,  r.origen, r.destino, b.placa, b.tipo, p.nombre, p.apellido, p.cedula, t.cantidad, t.fecha_viaje, t.hora_salida 
                FROM tiquetes t 
                INNER JOIN pasajero p ON p.id = t.id_pasajero
                INNER JOIN ruta r ON r.id= t.id_ruta 
                INNER JOIN bus b ON b.id= t.id_bus
                """
            cursor.execute(sql)
            tiquetes = cursor.fetchall()
            conn.close()
        return tiquetes
    except:
        print("An exception occurred")

# -------------- Funcion para mosrtar un pasajero en especifico---------------------- #
def consultarTiquete(id):
    conn = mysqlConnect()
    tiquetes = []
    with conn.cursor() as cursor:
        sql = "select id, cantidad, fecha_viaje, hora_salida, id_bus, id_pasajero, id_ruta from tiquetes where id = %s"
        cursor.execute(sql, id)
        tiquetes = cursor.fetchone()
        conn.close()
    return tiquetes

# -------------- Funcion para Borrar pasajero---------------------- #
def borrarTiquete(id):
    conn = mysqlConnect()
    with conn.cursor() as cursor:
        sql = "delete from tiquetes where id = %s"
        cursor.execute(sql, (id))
        conn.commit()
        conn.close()
    
#-------------------TRaer tiquetes por el id---------------#

def getTiqueteById(id):
    try :
        conn = mysqlConnect()
        tiquete = []
        with conn.cursor() as cursor:
            sql = """SELECT t.id as id_tiquete,  r.id as id_ruta, b.id as id_bus, p.id as id_pasajero, t.cantidad, t.fecha_viaje, t.hora_salida 
                FROM tiquetes t 
                INNER JOIN pasajero p ON p.id = t.id_pasajero
                INNER JOIN ruta r ON r.id= t.id_ruta 
                INNER JOIN bus b ON b.id= t.id_bus
                WHERE t.id = %s
                """
            cursor.execute(sql, (id))
            tiquete = cursor.fetchone()
            conn.close()
        return tiquete
    except:
        print("An exception occurred")

#-------------------Select de rutas---------------#

