import random
import getpass

# Variables
listaUsuario = []
listaContrasena = []
listaNombre = []
listaDivisa = []

# Load user information from a text file
def loaduserData():
    try:
        with open("user_data.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                username, password, name, balance = line.strip().split(",")
                listaUsuario.append(username)
                listaContrasena.append(password)
                listaNombre.append(name)
                listaDivisa.append(float(balance))
        return True
    except FileNotFoundError:
        return False


def saveuserData():
    with open("user_data.txt", "w") as file:
        for i in range(len(listaUsuario)):
            file.write(f"{listaUsuario[i]},{listaContrasena[i]},{listaNombre[i]},{listaDivisa[i]}\n")

def registroUsuario():
    listaUsuario = []
listaContrasena = []
listaNombre = []
listaDivisa = []


def registroUsuario() :
    username = ""
    contador = 0
    while len(username) < 5 :
        username = input("Ingrese su nombre su usuario: ")
        if len(username) < 5 :
            print("Por favor, ingrese un usuario con 5 caracteres o mas")
            contador += 1 
        else:
            listaUsuario.append(username)
        if contador == 3 :
            print("Ha alcanzado el limite de intentos")
            return
    
    name = input("Ingrese su nombre:")
    listaNombre.append(name)

    password = ""
    while len(password) < 6 :
        password = getpass.getpass("Ingrese su contraseña: ")
        if len(password) < 6 :
            print("Por favor, ingrese una contraseña de 6 caracteres o mas")
        else:
            listaContrasena.append(password)
    monto = 0 
    balance = ""
    contador = 0
    while monto < 100:
            divisa = ""
        
            
            print("Realice su deposito")
            print("1. Dolares")
            print("2. Colones")
            print("3. Bitcoin")

            divisa = int(input("Seleccione una divisa: "))

            if divisa == 1:
                print("1.Dolares")
                balance = float(input("Ingrese un monto a depositar en su cuenta: "))
                contador += 1 
                monto = balance

            elif divisa == 2:
                print("2.Colones")
                balance = float(input("Ingrese un monto a depositar en su cuenta: "))
                contador += 1 
                monto = balance / 538

            elif divisa == 3:
                print("3.Bitcoin")
                balance = float(input("Ingrese un monto a depositar en su cuenta: "))
                contador += 1 
                monto = balance * 26755

            else: 
                print("Por favor, seleccione una opcion valida")

            if contador == 3:
                print("Limite alcanzado en el deposito, por favor vuelva a iniciar")
                listaContrasena.pop()
                listaNombre.pop()
                listaUsuario.pop()
                return
    listaDivisa.append(monto)

    print("Transaccion realizada satisfactoriamente, su saldo es de: "+str(monto)+" dolares ")


opcion = ""


def dreamworldCasino():
     
    while True:
        print("Menú de Juegos:")
        print("1. Tragamonedas")
        print("2. Blackjack")
        print("3. Volver al menú principal")

        gameChoice = input("Seleccione un juego: ")

        if gameChoice == "1":
            print("Jugar tragamonedas()")
        elif gameChoice == "2":
            balance = blackjack_game(balance)
        elif gameChoice == "3":
            print("Saliendo del casino.")
            listaDivisa[listaUsuario.index(username)] = balance
            break
        else:
            print("Opción inválida.")


def blackjack_game(balance):

 def main():
    if not loaduserData():
        print("No hay usuarios registrados. Por favor, regístrese primero.")
        return

    global username
    username = input("Ingrese su usuario: ")
    password = getpass.getpass("Ingrese su contraseña: ")

    max_attempts = 3
    while max_attempts > 0:
        if username in listaUsuario and password == listaContrasena[listaUsuario.index(username)]:
            print(f"Bienvenido, {listaNombre[listaUsuario.index(username)]}!")
            break
        else:
            max_attempts -= 1
            print(f"Usuario o contraseña incorrectos. Intentos restantes: {max_attempts}")
            if max_attempts == 0:
                print("Se excedió el máximo de intentos para ingresar su ID, volviendo al menú principal.")
                return

while opcion != "4":
    print("Bienvenido al menú:")
    print("1. Registro de usuario nuevo")
    print("2. DreamWorld Casino")
    print("3. Configuración Avanzada")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registroUsuario()
    elif opcion == "2":
        dreamworldCasino()
    elif opcion == "3":
        print("configuracionavanzada()")
    elif opcion == "4":
        print("Gracias por participar")
    else:
        print("Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

