from modelos.libro import Libro
from modelos.cliente import Cliente
from servicios.gestor_db import GestorDB

def menu_principal():
    gestor = GestorDB()
    
    while True:
        print("\n" + "="*40)
        print(" 📚 SISTEMA DE GESTIÓN BIBLIOTECARIA ")
        print("="*40)
        print("1. Registrar nuevo LIBRO")
        print("2. Registrar nuevo CLIENTE")
        print("3. REALIZAR PRÉSTAMO")
        print("4. DEVOLVER LIBRO")
        print("5. VER INVENTARIO Y USUARIOS")
        print("6. SALIR")
        
        opcion = input("\n👉 Selecciona una opción (1-6): ")

        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor: ")
            nuevo_id = gestor.generar_id("libros")
            libro = Libro(id=nuevo_id, titulo=titulo, autor=autor)
            datos = gestor.cargar_datos()
            datos["libros"].append(libro.to_dict())
            gestor.guardar_datos(datos)
            print(f"✅ Libro '{titulo}' guardado con ID: {nuevo_id}")

        elif opcion == "2":
            nombre = input("Nombre del cliente: ")
            correo = input("Correo: ")
            nuevo_id = gestor.generar_id("usuarios")
            cliente = Cliente(id=nuevo_id, nombre=nombre, correo=correo)
            datos = gestor.cargar_datos()
            datos["usuarios"].append(cliente.to_dict())
            gestor.guardar_datos(datos)
            print(f"✅ Cliente '{nombre}' guardado con ID: {nuevo_id}")

        elif opcion == "3":
            l_id = int(input("ID del Libro a prestar: "))
            c_id = int(input("ID del Cliente: "))
            datos = gestor.cargar_datos()
            libro = next((l for l in datos["libros"] if l["id"] == l_id), None)
            cliente = next((u for u in datos["usuarios"] if u["id"] == c_id), None)

            if libro and cliente:
                if libro["disponible"]:
                    libro["disponible"] = False
                    cliente["libros_prestados"].append(libro["titulo"])
                    gestor.guardar_datos(datos)
                    print(f"✅ ¡Préstamo exitoso! '{libro['titulo']}' -> {cliente['nombre']}")
                else:
                    print(f"⚠️ El libro '{libro['titulo']}' ya está prestado.")
            else:
                print("❌ Error: Libro o Cliente no encontrado.")

        elif opcion == "4":
            l_id = int(input("ID del Libro a devolver: "))
            c_id = int(input("ID del Cliente: "))
            datos = gestor.cargar_datos()
            libro = next((l for l in datos["libros"] if l["id"] == l_id), None)
            cliente = next((u for u in datos["usuarios"] if u["id"] == c_id), None)

            if libro and cliente:
                if not libro["disponible"]:
                    libro["disponible"] = True
                    if libro["titulo"] in cliente["libros_prestados"]:
                        cliente["libros_prestados"].remove(libro["titulo"])
                    gestor.guardar_datos(datos)
                    print(f"✅ Devolución exitosa. '{libro['titulo']}' está disponible de nuevo.")
                else:
                    print("⚠️ Este libro ya estaba disponible.")
            else:
                print("❌ Error: Datos incorrectos.")

        elif opcion == "5":
            datos = gestor.cargar_datos()
            print("\n--- 📖 INVENTARIO ---")
            for l in datos["libros"]:
                estado = "✅" if l['disponible'] else "❌"
                print(f"ID: {l['id']} | {l['titulo']} - {estado}")
            print("\n--- 👤 USUARIOS ---")
            for u in datos["usuarios"]:
                prestados = ", ".join(u.get("libros_prestados", []))
                print(f"ID: {u['id']} | {u['nombre']} | Libros: [{prestados}]")

        elif opcion == "6":
            print("👋 ¡Cerrando sistema!")
            break

if __name__ == "__main__":
    menu_principal()