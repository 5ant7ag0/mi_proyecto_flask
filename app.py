from flask import Flask, render_template, request, redirect
from extensions import db
from config import Config
from models import Usuario, Libro, Prestamo 
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/")
def index():
    usuarios = Usuario.query.all()
    libros_disponibles = Libro.query.filter_by(estado="Disponible").all()
    todos_los_libros = Libro.query.all()
    # Solo mostramos préstamos que aún no han sido devueltos
    prestamos_activos = Prestamo.query.filter_by(fecha_devolucion=None).all()
    
    return render_template("index.html", 
                           usuarios=usuarios, 
                           libros=libros_disponibles, 
                           inventario=todos_los_libros,
                           prestamos=prestamos_activos)

@app.route("/registrar_usuario", methods=['POST'])
def registrar_usuario():
    nuevo = Usuario(
        cedula=request.form.get('cedula'),
        nombre=request.form.get('nombre'),
        apellido=request.form.get('apellido'),
        correo=request.form.get('correo')
    )
    db.session.add(nuevo)
    db.session.commit()
    return redirect("/")

@app.route("/registrar_libro", methods=['POST'])
def registrar_libro():
    nuevo = Libro(
        titulo=request.form.get('titulo'),
        autor=request.form.get('autor'),
        genero=request.form.get('genero')
    )
    db.session.add(nuevo)
    db.session.commit()
    return redirect("/")

@app.route("/realizar_prestamo", methods=['POST'])
def realizar_prestamo():
    u_cedula = request.form.get('usuario_cedula')
    l_id = request.form.get('libro_id')

    libro = Libro.query.get(l_id)
    if libro and libro.estado == "Disponible":
        nuevo_p = Prestamo(usuario_cedula=u_cedula, libro_id=l_id)
        libro.estado = "Prestado"
        db.session.add(nuevo_p)
        db.session.commit()
        
    return redirect("/")

@app.route("/devolver_libro/<int:id>")
def devolver_libro(id):
    prestamo = Prestamo.query.get(id)
    if prestamo:
        # 1. Marcar fecha de devolución
        prestamo.fecha_devolucion = datetime.utcnow()
        # 2. Poner el libro disponible de nuevo
        libro = Libro.query.get(prestamo.libro_id)
        libro.estado = "Disponible"
        
        db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5005)