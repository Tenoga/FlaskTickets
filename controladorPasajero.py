from DB import mysqlConnect

# -------------- Funcion para insertar un pasajero en la BD---------------------- #
def crearPasajero(nombre, apellido, cedula, correo, telefono):
    conn = mysqlConnect()
    with conn.cursor() as cursor:
        sql = "insert into pasajero (nombre, apellido, cedula, correo, telefono) Values(%s,%s,%s,%s,%s)"
        cursor.execute(sql, (nombre, apellido, cedula, correo, telefono))
        conn.commit()
        conn.close()

# -------------- Funcion para editar un pasajero en la BD---------------------- #
def editarPasajero(nombre, apellido, cedula, correo, telefono, id):
    conn = mysqlConnect()
    with conn.cursor() as cursor:
        sql = "update pasajero set nombre= %s, apellido= %s, cedula = %s, correo= %s, telefono= %s where id = %s;"
        cursor.execute(sql, (nombre, apellido, cedula, correo, telefono, id))
        conn.commit()
        conn.close()

# -------------- Funcion para consultar todos los valores de pasajeros en la BD---------------------- #
def consultarClientes():
    conn = mysqlConnect()
    usuarios = []
    with conn.cursor() as cursor:
        sql = "select * from pasajero"
        cursor.execute(sql)
        usuarios = cursor.fetchall()
        conn.close()
    return usuarios


# -------------- Funcion para mosrtar un pasajero en especifico---------------------- #
def consultarCliente(id):
    conn = mysqlConnect()
    usuarios = []
    with conn.cursor() as cursor:
        sql = "select id, nombre, apellido, cedula, correo, telefono from pasajero where id = %s"
        cursor.execute(sql, id)
        usuarios = cursor.fetchone()
        conn.close()
    return usuarios

# -------------- Funcion para Borrar pasajero---------------------- #
def borrarPasajero(id):
    conn = mysqlConnect()
    with conn.cursor() as cursor:
        sql = "delete from pasajero where id = %s"
        cursor.execute(sql, (id))
        conn.commit()
        conn.close()
    
