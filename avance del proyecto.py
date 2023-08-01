import os

def eliminar_usuario():
    user_id = input("Ingrese el ID del usuario que desea eliminar: ")
    user_folder = f"usuarios/{user_id}"

    if os.path.exists(user_folder):
        # Eliminar todos los registros (carpetas) asociadas al usuario
        try:
            os.rmdir(user_folder)
            print(f"El usuario con ID {user_id} ha sido eliminado exitosamente.")
        except OSError:
            print(f"No se pudieron eliminar los registros del usuario con ID {user_id}.")
    else:
        print(f"El usuario con ID {user_id} no existe.")

def modificar_valores_sistema():
    conversion_options = [
        "Tipo de cambio: Compra de dólares usando colones",
        "Tipo de cambio: Compra de dólares usando bitcoins",
        "Valor acumulado Tragamonedas",
        "Apuesta mínima Tragamonedas",
        "Apuesta mínima Blackjack",
        "Inversión mínima para registrarse"
    ]
    print("¿Qué desea modificar?")
    for idx, option in enumerate(conversion_options, start=1):
        print(f"{idx}. {option}")
    print("7. Salir")

    selected_option = int(input("Ingrese el número correspondiente al factor que desea modificar: "))

    if 1 <= selected_option <= 6:
        # Realizar la modificación/actualización del archivo correspondiente
        print(f"Modificación del factor {conversion_options[selected_option-1]} realizada con éxito.")
    elif selected_option == 7:
        return
    else:
        print("Opción inválida. Por favor, ingrese un número válido.")

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Eliminar usuario")
        print("2. Modificar valores del sistema")
        print("3. Salir")

        try:
            opcion = int(input("Ingrese el número de la opción que desea seleccionar: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if opcion == 1:
            eliminar_usuario()
        elif opcion == 2:
            modificar_valores_sistema()
        elif opcion == 3:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    menu_principal()
