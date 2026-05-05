from .base import Base

class Usuario(Base):
    def __init__(self, id: int = None, nombre: str = None, correo: str = None):
        # Herencia: enviamos el ID a la clase Base
        super().__init__(id)
        
        # Atributos comunes para cualquier persona en el sistema 
        self.nombre = nombre
        self.correo = correo