from extensions import db
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = 'Usuario'
    cedula = db.Column(db.String(10), primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(100), unique=True)

class Libro(db.Model):
    __tablename__ = 'Libro'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(50))
    estado = db.Column(db.String(20), default="Disponible")

class Prestamo(db.Model):
    __tablename__ = 'Prestamo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha_prestamo = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_devolucion = db.Column(db.DateTime, nullable=True) # <--- Nuevo campo
    
    usuario_cedula = db.Column(db.String(10), db.ForeignKey('Usuario.cedula'), nullable=False)
    libro_id = db.Column(db.Integer, db.ForeignKey('Libro.id'), nullable=False)

    usuario = db.relationship('Usuario', backref='prestamos')
    libro = db.relationship('Libro', backref='prestamos')