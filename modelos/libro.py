from .base import Base

class Libro(Base):
    def __init__(self, id: int = None, titulo: str = None, autor: str = None, año: int = None, editorial: str = None):
        # Herencia: super() inicializa el id en la clase Base
        super().__init__(id)
        
        # Atributos específicos del libro
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.editorial = editorial
        
        # Estado del libro: clave para validar préstamos
        self.disponible = True

    def mostrar_info(self):
        """Muestra la información básica del libro (Polimorfismo) [cite: 127]"""
        estado = "Disponible" if self.disponible else "Prestado"
        return f"ID: {self.id} | {self.titulo} - {self.autor} ({estado})"