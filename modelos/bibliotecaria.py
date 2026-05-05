from .usuario import Usuario

class Bibliotecaria(Usuario):
    def __init__(self, id: int = None, nombre: str = None, correo: str = None, empleado_id: str = None):
        # Herencia: enviamos nombre y correo a la clase Usuario
        super().__init__(id, nombre, correo)
        
        # Atributo único para el personal de la biblioteca
        self.empleado_id = empleado_id

    def administrar_libro(self):
        """Acción específica de administración (Polimorfismo)"""
        return f"La bibliotecaria {self.nombre} está gestionando el inventario."