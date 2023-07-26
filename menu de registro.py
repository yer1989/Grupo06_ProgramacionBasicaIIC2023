# Definición de la estructura de datos para gestionar la información de los usuarios
# Puedes modificar esta estructura según los datos que necesites almacenar para cada usuario.
usuarios = []

def registrar_usuario(nombre, correo, contraseña):
    nuevo_usuario = {
        'nombre': nombre,
        'correo': correo,
        'contraseña': contraseña
    }
    usuarios.append(nuevo_usuario)
    print("¡Usuario registrado con éxito!")

def mostrar_usuarios():
    print("Lista de usuarios registrados:")
    for usuario in usuarios:
        print(f"Nombre: {usuario['nombre']}, Correo: {usuario['correo']}")

# Función para el menú principal
def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar nuevo usuario")
        print("2. Mostrar usuarios registrados")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del nuevo usuario: ")
            correo = input("Ingrese el correo del nuevo usuario: ")
            contraseña = input("Ingrese la contraseña del nuevo usuario: ")
            registrar_usuario(nombre, correo, contraseña)

        elif opcion == '2':
            mostrar_usuarios()

        elif opcion == '3':
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    # Llamamos a la función del menú principal cuando se ejecute el script.
    menu_principal()
