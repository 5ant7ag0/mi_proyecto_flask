class Base: #se crea una clase base para heredar atributos y métodos de otras clases
    def __init__(self, id: int = None):
        # Encapsulamiento: El ID se asigna automáticamente si no se provee uno
        self.id = id

    def to_dict(self) -> dict:
        """
        Convierte los atributos de cualquier objeto que herede de Base 
        en un diccionario. Esto es esencial para guardar en JSON.
        """
        # vars(self) devuelve los atributos del objeto como un diccionario
        return vars(self)