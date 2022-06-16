from flask import Flask, render_template, request, redirect
import controladorPasajero,  controladorTiquetes, controladorBuses, controladorRutas
app = Flask(__name__)

# -------------- GET Index---------------------- #
@app.route('/')
def index():
    return render_template("index.html")

# -------------- GET about---------------------- #
@app.route('/about')
def about():
    return render_template("about.html")

# -------------- GET Contactenos---------------------- #
# @app.route('/contactenos')
# def contactenos():
#     return render_template("contactenos.html")
    
# -------------- Get Pasajero---------------------- #
@app.route('/crearpasajero')
def crearpasajeroGet():
    return render_template("crearpasajero.html")

# -------------- POST Pasajero---------------------- #
@app.route('/crearpasajero', methods = ['POST'])
def crearpasajeroPost():
    if request.method == 'POST':
        txtNombre = request.form['nombre']
        txtApellido = request.form['apellido']
        txtCedula = request.form['cedula']
        txtCorreo = request.form['correo']
        txtTelefono = request.form['telefono']
        controladorPasajero.crearPasajero(txtNombre, txtApellido, txtCedula, txtCorreo, txtTelefono)
    else:
        print('Error al guardar usuario')
    return redirect("/mostrarpasajeros")

# -------------- GET Lista pasajeros---------------------- #
@app.route('/mostrarpasajeros')
def mostrarpasajerosGet():
    pasajeros =  controladorPasajero.consultarClientes()
    return render_template("mostrarpasajeros.html", pasajeros = pasajeros)

# --------------  Edit Pasajero---------------------- #
@app.route('/editpasajero/<int:id>', methods = ['POST', 'GET'])
def editpasajeroGet(id):
    pasajero = []
    if request.method == 'POST':
        txtNombre = request.form['nombre']
        txtApellido = request.form['apellido']
        txtCedula = request.form['cedula']
        txtCorreo = request.form['correo']
        txtTelefono = request.form['telefono']
        controladorPasajero.editarPasajero(txtNombre, txtApellido, txtCedula, txtCorreo, txtTelefono, id)
        return redirect("/mostrarpasajeros")
    else:
        pasajero = controladorPasajero.consultarCliente(id)
    return render_template("/editpasajero.html", usuario = pasajero)

#----------------edit TIQUETES ------------------------# 

@app.route('/editTiquete/<int:id>', methods=['GET', 'POST'])
def editTiquete(id):
    if request.method == 'POST':
        rutas = request.form['ruta']
        buses = request.form['bus']
        id_pasajero = request.form['pasajero']
        cantidad = request.form['cantidad']
        fecha_viaje = request.form['fecha_viaje']
        hora_salida = request.form['hora_salida']
        controladorTiquetes.editarTiquetes(cantidad, fecha_viaje, hora_salida, buses, id_pasajero, rutas, id)
        return redirect('/mostrartiquetes')
    elif request.method == 'GET':
        tiquete = controladorTiquetes.getTiqueteById(id)
        rutas = controladorRutas.consultarRutas()
        buses = controladorBuses.consultarBuses()
        pasajeros = controladorPasajero.consultarClientes()
        return render_template('editTiquete.html', tiquete = tiquete, rutas = rutas, buses = buses, pasajeros = pasajeros)


# -------------- BORRAR Pasajero---------------------- #
@app.route('/borrarPasajero/<int:id>')
def eliminarPasajero(id):
    controladorPasajero.borrarPasajero(id)
    return redirect("/mostrarpasajeros")

# -------------- GET Ver lista Tiquetes---------------------- #
@app.route('/mostrartiquetes')
def tiquetes():
    tiquetes = controladorTiquetes.consultarTiquetes()
    return render_template("mostrartiquetes.html", tiquetes = tiquetes)
# -------------- GET Comprar tiquete---------------------- #

@app.route('/buytiquete', methods=['GET', 'POST'])
def buy_tickets():
    if request.method == 'POST':
        cantidad = request.form['cantidad']
        fecha_viaje = request.form['fecha_viaje']
        hora_salida = request.form['hora_salida']
        id_bus = request.form['bus']
        id_pasajero = request.form['pasajero']
        id_ruta = request.form['ruta']
        controladorTiquetes.crearTiquetes(cantidad, fecha_viaje, hora_salida, id_bus, id_pasajero, id_ruta)
        return redirect('/mostrartiquetes')
    elif request.method == 'GET':
        rutas = controladorRutas.consultarRutas()
        buses = controladorBuses.consultarBuses()
        pasajeros = controladorPasajero.consultarClientes()
        return render_template('buytiquete.html', rutas = rutas, buses = buses, pasajeros = pasajeros)
# -------------- GET Ver Tiquete---------------------- #
@app.route('/vertiquete')
def vertiquete():
    return render_template("vertiquete.html")


# -------------- BORRAR Tiquetes---------------------- #
@app.route('/borrarTiquete/<int:id>')
def eliminarTiquete(id):
    controladorTiquetes.borrarTiquete(id)
    return redirect("/mostrartiquetes")


@app.route('/mostrarbuses')
def mostrarbusesGet():
    buses =  controladorBuses.consultarBuses()
    return render_template("mostrarbuses.html", buses = buses)

@app.route('/borrarBus/<int:id>')
def eliminarBus(id):
    controladorBuses.borrarBus(id)
    return redirect("/mostrarbuses")

@app.route('/mostrarRutas')
def mostrarrutasGet():
    rutas =  controladorRutas.consultarRutas()
    return render_template("mostrarrutas.html", rutas = rutas)

@app.route('/borrarRuta/<int:id>')
def eliminarRutas(id):
    controladorRutas.borrarRutas(id)
    return redirect("/mostrarRutas")

# -------------- un login ---------------------- #
@app.route('/login', methods=['GET', 'POST'])
def login():
 if request.method == 'POST':
        nombre = request.form['nombre']
        print(nombre)
        return f"Bienvenido: {nombre}, tu nombre ha sido guardado"
 else:
        return "Lo sentimos, no se pudo guardar tu nombre"

if __name__ == '__main__':
    app.run(port = 3000, debug = True, host = '0.0.0.0')






