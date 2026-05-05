import json
import os

class GestorDB:
    def __init__(self, archivo='biblioteca.json'):
        self.archivo = archivo
        # Si el archivo no existe, lo crea con una estructura inicial vacía
        if not os.path.exists(self.archivo):
            self.guardar_datos({"libros": [], "usuarios": []})

    def cargar_datos(self):
        """Lee el archivo JSON y devuelve un diccionario con la info."""
        with open(self.archivo, 'r') as f:
            return json.load(f)

    def guardar_datos(self, datos):
        """Escribe el diccionario actual en el archivo JSON."""
        with open(self.archivo, 'w') as f:
            json.dump(datos, f, indent=4)

    def generar_id(self, categoria):
        """
        Lógica de ID Automático: Cuenta cuántos elementos hay 
        en 'libros' o 'usuarios' y le suma 1.
        """
        datos = self.cargar_datos()
        return len(datos.get(categoria, [])) + 1