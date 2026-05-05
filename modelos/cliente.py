from .usuario import Usuario

class Cliente(Usuario):
    def __init__(self, id: int = None, nombre: str = None, correo: str = None):
        # Herencia: enviamos los datos al padre (Usuario)
        super().__init__(id, nombre, correo)
        
        # Lista para rastrear qué libros tiene este cliente (Encapsulamiento)
        self.libros_prestados = []

    def consultar_libro(self, titulo: str):
        """Acción específica del cliente (Polimorfismo)"""
        return f"El cliente {self.nombre} está buscando el libro: {titulo}"