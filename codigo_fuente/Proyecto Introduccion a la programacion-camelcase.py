#Proyecto Introduccion a la programacion 
#Autor Grupo 6 
#Problema Crear un programa que tenga un menu con 4 opciones para un casino crear un usuario y registrar, se debe solicitar al usuario que desea realizar

#Se importan las librerías que permiten crear un password; crear y leer archivos (entre otras operaciones con archivos); crear números aleatorios y funciones relacionadas con el tiempo (que permitirán incluir intervalos de tiempo de respuesta)
import getpass 
import os
import random
import time
import shutil


#Variables
listaUsuario = []
listaContrasena = []
listaNombre = []
listaDivisa = []

#Esto es a lo que se le llama un "diccionario" y nos permite almacenar información y usar las definiciones como argumentos de otras funciones
usuario = {
    "usuario": "",
    "contrasena": "",
    "nombreusuario":"",
    "dinerocuenta": ""
}
configAvanzada = []
pinConfigAvanzada = ""

def cargaConfigAvanzada():
#Definimos el archivo en el que vamos a almacenar la información, que en este caso es llamado "configuración_avanzada.txt"
    nombreArchivo = "configuracion_avanzada.txt"

    carpetaPadre = os.path.abspath(os.path.dirname(__file__))

    rutaArchivo = os.path.join(carpetaPadre, "..", nombreArchivo)
#estos dos últimos métodos permiten establecer la ruta de la carpeta en la que se encuentra el archivo actual de ejecución del script y la ruta absoluta de la carpeta.
    global configAvanzada # la variable configAvanzada se utilizará para almacenar las líneas leídas desde el archivo
    try:
        with open(rutaArchivo, 'r') as archivo:
            configAvanzada = archivo.readlines() # este método permite leer todas las líneas del archivo y almacenarlas en la variable
        
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo: {nombreArchivo}")
    except IOError:
        print(f"Error al leer el archivo: {nombreArchivo}")

#La siguiente función crea un nuevo usuario usando el diccionario definido antes, que tiene la información del usuario
def crearUsuario(usuario) : 
    try:
        nombreCarpeta = str(usuario["usuario"]) #Se convierte la información en un string

        carpetaPadre = os.path.join(os.getcwd(), os.pardir, nombreCarpeta)

        if not os.path.exists(carpetaPadre):
            os.makedirs(carpetaPadre)
        else:
            return 0
# Lo anterior construye la ruta de la carpeta padre utilizando el nombre del usuario, se verifica si la carpeta ya existe. Si no existe, se crea. Si la carpeta ya existe, la función devuelve 0 (el usuario ya existe)
       
        nombreArchivo = "saldos.txt"

        rutaArchivo = os.path.join(carpetaPadre, nombreArchivo)

        with open(rutaArchivo, "w") as archivo:
            archivo.write(str(round(float(usuario["dinerocuenta"]),2)))
# Se construye la ruta del archivo "saldos.txt". Luego, se escribe el saldo de la cuenta del usuario

        nombreArchivo = "usuarios_pines.txt"

        carpetaActual = os.path.abspath(os.path.dirname(__file__))

        rutaArchivo = os.path.join(carpetaActual, "..", nombreArchivo)
        with open(rutaArchivo, "a") as archivo:
            archivo.write("\n" + str(usuario["usuario"]) + "\n" + str(usuario["contrasena"] + "\n" +str(usuario["nombreusuario"])))
# Se construye la ruta del archivo "usuarios_pines.txt". Luego, se abre el archivo y se escribe la información del usuario

        return 1  # 1 para registro exitoso
    except Exception as e:
        return 0

# La siguiente función permite al usuario registrarse en el sistema
def registroUsuario() :
    op = "" # Almacena las opciones ingresadas por el usuario
    contador = 0 # Permite contar los intentos fallidos, y con la siguiente estructura cíclica se solicita la información al usuario (nombre de usuario). Si el usuario falla cinco veces habrá alcanzado el límite de intentos
    while len(op) < 5 :
        op = input("Ingrese su usuario: ")
        if len(op) < 5 :
            print("Por favor, ingrese un usuario con 5 caracteres o mas")
            contador += 1 
        else:
            listaUsuario = consultarUsuarios()
            for fila in listaUsuario:
                if fila[0] == op:
                    print("Usuario ya existe por favor reintente nuevamente")
                    contador += 1 
                    op = ""
                    break

            usuario["usuario"] = op
        if contador == 3 :
            print("Ha alcanzado el limite de intentos")
            return

    op = "" # Se usa la misma estructura que en el caso anterior, pero en este caso la estructura cíclica se repite hasta que el usuario ingrese una contraseña de más de 6 caracteres. Luego pide la confirmación de la contraseña
    
    while len(op) < 6 :
        op= getpass.getpass("Ingrese su contraseña: ")
        if len(op) < 6 :
            print("Por favor, ingrese una contraseña de 6 caracteres o mas")
        else:
            passw = ""
            while op != passw :
                passw= getpass.getpass("Ingrese su contraseña nuevamente: ")
                if len(op) < 6 :
                    print("Por favor, ingrese una contraseña de 6 caracteres o mas")
                elif op == passw :
                    usuario["contrasena"] = passw
                else:
                    print("Contraseña no coincide con la anterior ingresada, por favor intente nuevamente")
#ciclo que se repite hasta que el usuario ingrese un nombre
    op = ""
    
    while len(op.strip()) == 0 :
        op= input("Ingrese su nombre: ")
        if len(op.strip()) == 0 :
            print("Por favor, ingrese un nombre, el campo no puede quedar vacio.")
        else:
            usuario["nombreusuario"] = op

    monto = 0  # Se crea la variable "monto" y con el siguiente ciclo se solicita al usuario que ingrese un monto
    op = ""
    contador = 0 #Este contador mide el número de intentos
    while monto < int(configAvanzada[5].strip()):
            divisa = ""

#Se le solicita al usuario que escoja el tipo de divisa, y dependiendo de la divisa se establece el monto mínimo
            print(f"Realice su deposito, el deposito debe ser mayor o igual a {configAvanzada[5].strip()}")
            print("1. Dolares")
            print("2. Colones")
            print("3. Bitcoin")

            divisa = int(input("Seleccione una divisa: "))

            if divisa == 1:
                print("1.Dolares")
                op = float(input("Ingrese un monto a depositar en su cuenta: "))
                contador += 1 
                monto = op

            elif divisa == 2:
                print("2.Colones")
                op = float(input("Ingrese un monto a depositar en su cuenta: "))
                contador += 1 
                monto = op / int(configAvanzada[0].strip())

            elif divisa == 3:
                print("3.Bitcoin")
                op = float(input("Ingrese un monto a depositar en su cuenta: "))
                contador += 1 
                monto = op * int(configAvanzada[1].strip())

            else: 
                print("Por favor, seleccione una opcion valida.")

            if monto < int(configAvanzada[5].strip()):
                print(f"Monto a depositar no puede ser menor a {configAvanzada[5].strip()}, por favor intente de nuevo.")

            if contador == 3:
                print("Limite alcanzado en el deposito, por favor vuelva a iniciar.")
                return
    usuario["dinerocuenta"] = monto #El monto se guarda en el diccionario creado para el usuario ("usuario"), bajo "dinerocuenta"

    if crearUsuario(usuario) == 1 : #En el caso de que el registro haya sido exitoso (en la función anterior), y el monto guardado, se imprime el siguiente mensaje
        print(f"Transaccion realizada satisfactoriamente, su saldo es de: ${str(monto)}.")
    else :
        print("Error al guardar el usuario.")

def dreamWorldCasino():
    listaUsuario = consultarUsuarios() # Tomamos la información de usuario llamando a la función "consultarUsuarios" que sigue a esta función
    validaUsuario = 0
    contador = 0 
    usrList = [] # Guarda la información de usuario válido en una lista

    if len(listaUsuario)>0:
        op = ""
        while len(op) < 5 :
            op = input("Ingrese su usuario: ")
        if len(op) < 5 :
            print("Por favor, ingrese un usuario con 5 caracteres o mas")
            contador += 1 
# Si el nombre de usuario no cumple con el requisito de 5 caracteres mínimo, se repite el ciclo y se solicita la información de nuevo y se incrementa el contador de intentos
        else:
            for fila in listaUsuario:
                if fila[0] == op:
                    usrList.append(fila[0])
                    usrList.append(fila[1])
                    usrList.append(fila[2])
                    validaUsuario = 1 # Si el usuario existe, se asigna 1 a "validaUsuario"
                    break
   # Si el nombre de usuario cumple con el mínimo, se agrega a la lista temporal              
            if validaUsuario == 0:
                contador += 1 
                print("Usuario no existe por favor reintente nuevamente")
        if contador == 3 :
            print("Se excedió el máximo de intentos para ingresar su usuario, volviendo al menú principal")
            return
    else:
        print("No hay usuarios registrados en el sistema")

    contador = 0 
    if validaUsuario == 1: #Dado que el nombre de usuario es correcto el usuario debe ingresar su pin, que debe tener 6 caracteres mínimo. Si no cumple con este requisito, se muestra un mensaje y se incrementa el contador de intentos.
        op = ""
        while len(op) < 6 :
            op = getpass.getpass("Ingrese el pin del usuario: ")
        if len(op) < 6 :
            print("Por favor, ingrese un pin con 6 caracteres o mas")
            contador += 1 
        else:
            if usrList[1] == op: # Si el pin coincide con el almacenado en la lista entonces el valor se mantiene en 1
                validaUsuario = 1
            else:
                validaUsuario = 0
            if validaUsuario == 0:
                contador += 1 
                print("PIN incorrecto por favor reintente nuevamente")
        if contador == 3 :
            print("Se excedió el máximo de intentos para ingresar su PIN, volviendo al menú principal")
            return
    
    if validaUsuario == 1: # Si "validaUsuario" es igual a 1, entonces el usuario entre a DreamWorld Casino, y se despliega el menú
        print("Bienvenido " + usrList[0] + " a DreamWorld Casino!")
        opcion = "" # En esta variable se guarda la opción que se escoge en el menu. El usuario seguirá en el menú (por medio de la ciclo while, que sigue hasta que el usuario desee salir)

        while opcion != "6":

            saldo = consultarSaldo(usrList[0]) # Recuperamos el saldo del usuario asociado a su nombre
            if saldo == "error":
                print("Se ha presentado un error obteniendo el saldo.")
                break
            elif len(usrList) == 3 : # Si longitud de ursList es igual a 3, entonces no hay un saldo para ese usuario aún
                usrList.append(float(saldo))
            else:
                usrList[3] = float(saldo) # Se extrae el saldo (cuarta posición en la lista)

            print("1. Retirar dinero")
            print("2. Depositar dinero")
            print("3. Ver saldo actual")
            print("4. Juegos en línea")
            print("5. Eliminar usuario")
            print("6. Salir")

            opcion = input("Seleccione una opción: ")
# Dependiendo de la opción escogida por el usuario, se llama a las funciones correspondientes
            if opcion == "1":
                retirarDinero(usrList)
            elif opcion == "2":
                depositarDinero(usrList)
            elif opcion == "3":
                print(f"Su saldo actual es de: {str(usrList[3])}.")
            elif opcion == "4":
                opcJuego = ""
                while opcJuego != "3":
                    saldo = consultarSaldo(usrList[0])
                    if saldo == "error":
                        print("Se ha presentado un error obteniendo el saldo.")
                        break
                    else:
                        usrList[3] = float(saldo)

                    if float(usrList[3])==0:
                        print("Usuario no tiene saldo disponible, por favor realizar un deposito.")
                        break
# Si el usuario escoge lo juegos en línea, entonces se le presenta las tres opciones que ofrece DreamWorld Casino                    
                    print("1. Blackjack")
                    print("2. Tragamonedas")
                    print("3. Salir")

                    opcJuego = input("Seleccione una opción: ")
                    if opcJuego == "1":
                        print("Reglas juegoBlackJack") # Se imprimen las reglas del BlackJack
                        print("PASO 1, Únete a una mesa, y haz tu apuesta. Una vezrecibe dos cartas boca arriba. El crupier también se reparte dos cartas, una descubierta y la otra boca abajo.")
                        print("PASO 2 Decide si pides o te plantas,tras analizar el valor de tu mano y todas las cartas que se han repartido, el siguiente paso es conseguir la mejor opción de estar lo más cerca posible del 21 sin pasarte.")
                        print("Pide carta=Pide otra carta al crupier. Hazlo cuando, según el valor actual de tus cartas, o bien estás seguro de que la próxima carta no hará que te pases, o estás dispuesto a correr el riesgo de que el crupier consiga una mano mejor.")
                        print("Plántate=Pide al crupier que pase al siguiente jugador y que no te reparta más cartas. Probablemente hagas esto cuando el valor de tus cartas ya es bastante alto (por ejemplo, más de 17) y no puedas estar seguro de que la mano del crupier vaya a superar a la tuya.")
                        print("PASO 3 El valor de tu mano, Como resultado del movimiento que acabas de hacer, tu mano probablemente tenga un nuevo valor. Sigues en el juego si tu mano vale 21 o menos.")
                        print("PASO 4 El crupier enseña sus cartas,cuando todos los jugadores de la mesa han tomado su decisión, el crupier muestra la carta que tenía boca abajo.")
                        print("PASO 5 Comprueba quién está más cerca de 21, Si tu mano está más cerca de 21 que la del crupier, superas al repartidor y ganas. Si el crupier tiene 21 o una puntuación más cercana a 21 que el resto de los jugadores, el crupier gana. El crupier te entregará tus ganancias si has tenido suerte. La cantidad del pago dependerá del tipo de apuesta que hayas hecho.")
                        juegoBlackJack(usrList)
                    elif opcJuego == "2":
                        print("Reglas MaquinaTragamonedas")
                        jugarMaquinaTragamonedas(usrList)
                    elif opcion == "3":
                        print("Volviendo al menú principal")
                    else:
                        print("Por favor, seleccione una opción válida.")
            elif opcion == "5":
                resultado = procesoEliminarUsuario(usrList)
                if resultado == "1":
                    break
                else:
                    print("No se pudo eliminar el usuario.")
            elif opcion == "6":
                print("Volviendo al menú principal")
            else:
                print("Por favor, seleccione una opción válida.")

def consultarSaldo(usuario):
    nombreArchivo = os.path.join(os.pardir, usuario, "saldos.txt") # Ruta al archivo "saldos.txt" dentro de un directorio que lleva el nombre del usuario (cada usuario tendrá su propia carpeta)

    def obtenerUltimoRegistro(archivo):
        with open(archivo, "r") as archivo_txt: # Abre el archivo en modo lectura
            lineas = archivo_txt.readlines() # Almacena todas las líneas del archivo en la variable "lineas"
            if lineas:
                return lineas[-1]
            else:
                return None

    saldo = obtenerUltimoRegistro(nombreArchivo)

    if saldo:
        return saldo.strip() 
    else:
        return "error"

# La siguiente función e encarga de leer y procesar información del archivo "usuarios_pines.txt" que contiene lo pines de usuarios
def consultarUsuarios():
    nombreArchivo = "usuarios_pines.txt"

    carpetaActual = os.path.abspath(os.path.dirname(__file__))

    rutaArchivo = os.path.join(carpetaActual, "..", nombreArchivo)
# La función utiliza "try" para abrir y leer el archivo "usuarios_pines.txt". Si el archivo no se encuentra, se da la excepción "FileNotFoundError", y si hay un error al leer el archivo, la excepción "IOError"
    try:
        with open(rutaArchivo, 'r') as archivo: # El archivo se abre en modo lectura
            usuarios = archivo.readlines()

        global pinConfigAvanzada 
        pinConfigAvanzada = str(usuarios[0].strip())

        del usuarios[0] # Se extrae esta línea y se almacena en la variable global pinConfigAvanzada. Luego, se elimina esta línea de la lista de usuarios

        listaUsuario = []
        for linea in range(0, len(usuarios), 3):
            usuario = usuarios[linea].strip()
            contrasena = usuarios[linea + 1].strip()
            nombreUsuario = usuarios[linea + 2].strip()
            listaUsuario.append([usuario, contrasena, nombreUsuario]) # Se extraen los valores de nombre de usuario, contraseña y nombre del usuario de las líneas y se almacenan en una lista listaUsuario

        return listaUsuario
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo: {nombreArchivo}")
    except IOError:
        print(f"Error al leer el archivo: {nombreArchivo}")

# Esta función, que recibe como argumento el diccionario "usuario", permite el retiro de dinero (o lo simula)
def retirarDinero(usuario):
    op = "" # En esta cadena se guardará la cantidad de dinero que el usuario quiere retirar
    contador = 0
    bandera = True # Esta variable va controlar la ejecución del ciclo while que hay a continuación
    print(f"{usuario[2]} tu saldo actual es de: {str(usuario[3])}.")
    while bandera :
        op = input("¿Cuanto desea retirar?: ")
        if float(op) == 0 or float(op) > float(usuario[3]) or float(op) < 0:
            print("Por favor, ingrese un monto correcto.")
            contador += 1 # Si la cantidad ingresada es igual a 0, mayor que el saldo disponible o menor que 0, se imprime un mensaje de error y se incrementa el contador en 1
        else:
            usuario[3] = float(usuario[3]) - float(op)
            actualizarSaldo(usuario)
            print(f"Su retiro de dinero ha sido exitoso, su saldo actual es de: {str(usuario[3])}.")
            bandera = False # Si la cantidad ingresada es válida se actualiza el saldo del usuario restando la cantidad ingresada

        if contador == 3 :
            print("Se excedió el máximo de intentos para realizar su retiro de dinero, volviendo al menú principal.")
            bandera = False # si el contador alcanzó el valor de 3, se imprime un mensaje indicando que se excedieron la cantidad máxima de intentos y se vuelve al menú
    return 0

# Esta función permite al usuario depositar dinero
def depositarDinero(usuario):

    divisa = ""
    monto = 0
# Estas variables se usarán para almacenar la opción de divisa seleccionada por el usuario y el monto que desea depositar
    
    print("Realice su deposito")
    print("1. Dolares")
    print("2. Colones")
    print("3. Bitcoin")
# Se solicita la información a usuario
    
    divisa = int(input("Seleccione una divisa: "))

    # Con cada una de las divisas (dependiendo de cuál escoge el usuario) se le solicita que haga el depósito
    if divisa == 1:
        print("1.Dolares")
        op = float(input("Ingrese un monto a depositar en su cuenta: "))
        monto = op

    elif divisa == 2:
        print("2.Colones")
        op = float(input("Ingrese un monto a depositar en su cuenta: "))
        monto = op / int(configAvanzada[0].strip())

    elif divisa == 3:
        print("3.Bitcoin")
        op = float(input("Ingrese un monto a depositar en su cuenta: "))
        monto = op * int(configAvanzada[1].strip())

    else: 
        print("Por favor, seleccione una opcion valida.")
        return

    usuario[3] = round(float(usuario[3]) + float(monto),2)
    actualizarSaldo(usuario) # Se llama a la función que sigue (actualizarSaldo), la cual actualiza el saldo del usuario sumando el monto ingresado al saldo actual del usuario
    print(f"Su deposito de dinero ha sido exitoso, {usuario[2]} su saldo actual es de: {str(usuario[3])}.")

def actualizarSaldo(usuario):
    nombreArchivo = "saldos.txt"

    nombreArchivo = os.path.join(os.pardir, usuario[0], "saldos.txt")

    rutaArchivo = os.path.join(nombreArchivo, "..", nombreArchivo)
    with open(rutaArchivo, "a") as archivo:
        archivo.write("\n" + str(round(usuario[3],2)))
    return 

def juegoBlackJack(usuario):

    saldo = float(usuario[3]) # Se extrae el saldo del usuario del cuarto elemento de la lista "usuario" y se almacena en la variable saldo.
    apuestaMinima = float(configAvanzada[4].strip()) # Se extrae la apuesta mínima requerida y se guarda en "apuestaMinima"

    while saldo >= apuestaMinima and True: # Se inicia un ciclo while que se ejecutará mientras el saldo del jugador sea mayor o igual a la apuesta mínima
        apuesta = float(input(f"{usuario[2]} tu saldo es {saldo}. ¿Cuánto deseas apostar? (mínimo {apuestaMinima}): "))
        if apuesta < apuestaMinima:
            print("Apuesta insuficiente. Debes apostar al menos el mínimo.")
            continue

        # Reparto inicial de cartas, se llama la siguiente función de este código, la cual genera las cartas de forma aleatoria, tanto para el usuario como para el crupier
        jugadorCartas = [generarCarta(), generarCarta()]
        crupierCartas = [generarCarta(), generarCarta()]

        mostrarCartasJugador(jugadorCartas) # Se llama a la función "mostrarCartasJugador" que está más adelante en este código y que muestra las cartas

        print(f"La primera carta del crupier es: {crupierCartas[0]}")

        # La siguiente función anidada llama a la función "puedeDividir" que está más adelante en el código. Si la función devuelve True, significa que el jugador tiene dos cartas del mismo valor y puede optar por dividir su mano. El programa pregunta al jugador si desea doblar su apuesta o dividir la jugada. Si no es posible dividir, solo se pregunta si desea doblar
        if puedeDividir(jugadorCartas):
            opcion = input("¿Deseas doblar tu apuesta 1 o dividir la jugada 2? ").upper()
        else:
            opcion = input("¿Deseas doblar tu apuesta 1? ").upper()

        if opcion == '1':
            if saldo >= apuesta * 2: # Si el usuario elige doblar su apuesta (opción 1), el programa verifica si el saldo es suficiente para realizar la apuesta duplicada. Si es posible, la apuesta se duplica y se actualiza la variable apuesta
                apuesta *= 2
                print(f"Apostaste el doble: {apuesta}")
            else:
                print("Saldo insuficiente para doblar la apuesta.")

        if puedeDividir(jugadorCartas): # Si el ususrio escoge la opción de dividir, se llama a la función dividirJugada (más adelante) para dividir su mano en dos manos separadas
            jugadorCartas, cartasJuego2, saldo = dividirJugada(jugadorCartas, saldo, apuesta)
            saldo = jugarRonda(jugadorCartas, crupierCartas, apuesta, saldo) # Se llama a la función jugarRonda para jugar una ronda con las cartas del jugador y del crupier (ver función más adelante)
            mostrarCartasJugador(cartasJuego2) # segunda ronda
            saldo = jugarRonda(cartasJuego2, crupierCartas, apuesta, saldo)
        else:
            saldo = jugarRonda(jugadorCartas, crupierCartas, apuesta, saldo) # El usuario no dividió la mano
        usuario[3] = saldo
        actualizarSaldo(usuario)

        print(f"{usuario[2]} tu saldo actual es de: {saldo}")

        opcion = input("¿Deseas seguir jugando 1 Sí o 2 No? ").upper()
        if opcion != '1':
            break



def generarCarta():
    naipes = ['Trébol', 'Diamantes', 'Corazones', 'Espadas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    naipe = random.choice(naipes)
    valor = random.choice(valores)
    return f"{valor} de {naipe}"

def valorMano(cartas):
    valores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 1}
    valor = sum(valores[carta.split()[0]] for carta in cartas)
    return valor

def mostrarCartasJugador(cartas):
    print("Tus cartas:")
    for carta in cartas:
        print(carta)

def puedeDividir(cartas):
    return len(cartas) == 2 and cartas[0].split()[0] == cartas[1].split()[0]

def dividirJugada(cartas, saldo, apuesta):
    if len(cartas) != 2 or cartas[0].split()[0] != cartas[1].split()[0]: # verifica si las cartas son iguales y por lo tanto se pueden dividir
        print("No puedes dividir la jugada en este momento.")
        return cartas, saldo

    if saldo < apuesta: # Si el saldo no es suficiente para dividir
        print("Saldo insuficiente para dividir la jugada.")
        return cartas, saldo

    nuevaCarta1 = generarCarta() # Se llama a la función generarCarta para generar las dos nuevas cartas en caso de que sí se pueda dividir
    nuevaCarta2 = generarCarta()

    print("Dividiendo la jugada...")
    print(f"Juego 1: {cartas[0]} y {nuevaCarta1}")
    print(f"Juego 2: {cartas[1]} y {nuevaCarta2}")

    cartasJuego1 = [cartas[0], nuevaCarta1] # Se combinan las nuevas cartas con las que ya habían
    cartasJuego2 = [cartas[1], nuevaCarta2]

    return cartasJuego1, cartasJuego2, saldo - apuesta

def jugarRonda(jugadorCartas, crupierCartas, apuesta, saldo):
    while True: # este ciclo se repite hasta que el jugador pierda o decida salir
        accion = input("¿Deseas pedir una nueva carta 1 o para detener el juego 2? ").upper()
        if accion == '1':
            nuevaCarta = generarCarta()
            print(f"Recibiste: {nuevaCarta}")
            jugadorCartas.append(nuevaCarta)
            mostrarCartasJugador(jugadorCartas)
            if valorMano(jugadorCartas) > 21:
                print("Te pasaste de 21. Pierdes.")
                saldo -= apuesta
                break
    # con el fragmente de código anterior, si el jugador elige pedir una nueva carta, se genera una nueva carta usando la función "generarCarta", se muestra al jugador, se agrega a la lista "jugadorCartas" y se muestra la mano actual. Si el valor total de la mano del jugador supera 21, el jugador pierde la ronda y se reduce el saldo en la cantidad de la apuesta, luego se rompe el ciclo
        elif accion == '2':
            break
        else:
            print("Opción no válida. Ingresa 1 para pedir una nueva carta o 2 para detener el juego.")

    if valorMano(jugadorCartas) <= 21: # Al detener el juego, esta función verifica el valor de las manos
        print("Turno del crupier...")
        print(f"La carta oculta del crupier es: {crupierCartas[1]}")
        while valorMano(crupierCartas) < 17: # El crupier pide carta en la medida en que sus cartas suman menos de 17
            nuevaCarta = generarCarta()
            print(f"El crupier recibe: {nuevaCarta}")
            crupierCartas.append(nuevaCarta)
        print("Cartas del crupier:")
        for carta in crupierCartas:
            print(carta)

        valorJugador = valorMano(jugadorCartas)
        valorCrupier = valorMano(crupierCartas)
        if valorJugador > 21 or (valorCrupier <= 21 and valorCrupier >= valorJugador):
            saldo -= apuesta
            print("El crupier gana.")
        elif valorCrupier > 21 or valorJugador > valorCrupier:
            saldo += apuesta
            print("¡Ganaste!")
        else:
            print("Empate. Se devuelve tu apuesta.")
# COn el fragmento anterior se comparan los valores de las cartas del usuario y del crupier para determinar quién gana
    print(f"Tu saldo actual es: {saldo}")
    return saldo


def mostrarMaquinaTragamonedas(figuras):
    print("Este es el resultado")
    time.sleep(1.5) # Con este método se hace pausa de 1.5 segundos, para dar la sensación de que la máquina está mostrando el resultado poco a poco
    for figura in figuras:
        print(figura, end=' ') # El ciclo "for" recorre cada elemento de la lista figuras. "End=' '" se utiliza para que la impresión de las figuras no salte de línea después de cada una, lo que crea la apariencia de estar impresas una al lado de la otra
        time.sleep(1.5)
    print()

def jugarMaquinaTragamonedas(usuario):
    saldoActual = usuario[3]
    apuestaMinima = float(configAvanzada[3].strip())
    cantidadJugadas = 1
    acumulado = float(configAvanzada[2].strip())

    while True:
        apuesta = float(input(f"{usuario[2]} cuanto desea apostar? Tu saldo es de: {saldoActual}: ")) #Se solicita al usuario la cantidad que desea apostar
        # la siguiente estructura de decisión determina si el usuario tiene un saldo mínimo que le permita jugar
        if saldoActual < apuestaMinima:
            print("No tienes suficiente dinero para jugar.")
            return
        if apuesta < apuestaMinima:
            print("El monto a apostar es menor a la apuesta mínima.")
        else:
            saldoActual -= apuesta

            print(f"Saldo actual: {saldoActual}")
            input("Presione Enter para jalar la palanca e iniciar el juego.")

            figuras = [random.choice(["@", "#", "+", "7"]) for _ in range(3)] # Símbolos aleatorios que van a servir para la máquina tragamonedas, se almacenan en la lista "figuras"

            figuras = ["@", "7", "#", "+"]
            if cantidadJugadas == 5:
                resultadoFigura = ["@"] * 3
            elif cantidadJugadas == 10:
                resultadoFigura = ["#"] * 3
            elif cantidadJugadas == 15:
                resultadoFigura = ["+"] * 3
            elif cantidadJugadas == 20:
                resultadoFigura = ["7"] * 3
                cantidadJugadas = 0
            else:
                resultadoFigura = [random.choice(figuras) for _ in range(3)] # Si no se cumple ninguna de las opciones anteriores, se generan figuras aleatorias

            mostrarMaquinaTragamonedas(resultadoFigura) # Se llama a la función anterior (más arriba en esta código) que permite mostrar el resultado
            
            # la siguiente estructura de decisión evalúa los diferentes resultados y establece el nuevo saldo dado los resultados
            if resultadoFigura.count("@") == 3:
                saldoActual += apuesta
                print("¡Recuperaste tu inversión!")
            elif resultadoFigura.count("#") == 3:
                saldoActual += apuesta * 2
                print("¡Ganaste el doble de tu inversión!")
            elif resultadoFigura.count("+") == 3:
                saldoActual += apuesta * 3
                print("¡Ganaste el triple de tu inversión!")
            elif resultadoFigura.count("7") == 3:
                saldoActual += acumulado
                acumulado = 0
                print("¡Ganaste el acumulado!")
            else:
                acumulado += apuesta

            cantidadJugadas += 1
            
            #Se actualizan los datos del usuario dados los resultados del juego
            usuario[3] = saldoActual
            actualizarSaldo(usuario)
            modificarConfigAvanzada(str(acumulado),3)
            cargaConfigAvanzada()

        print(f"{usuario[2]} tu saldo actual es de: {saldoActual}") # Se muestra el nuevo saldo al usuario
        jugarNuevamente = input("¿Deseas jugar nuevamente? (1 Sí o 2 No): ")
        if jugarNuevamente != '1':
            break


def modificarConfigAvanzada(linea, numeroLinea):
    nombreArchivo = "configuracion_avanzada.txt"

    carpetaActual = os.path.abspath(os.path.dirname(__file__))

    rutaArchivo = os.path.join(carpetaActual, "..", nombreArchivo)

    with open(rutaArchivo, 'r') as f:
        lineas = f.readlines() # Se lee todo el contenido del archivo y devuelve una lista en la que cada elemento es una línea del archivo, esto se le asigna a la variable "lineas"

    lineas[numeroLinea - 1] = str(linea) + '\n'

    with open(rutaArchivo, 'w') as f:
        f.writelines(lineas) # Se escriben todas las líneas modificadas en la lista "lineas" de nuevo en el archivo
    return


def procesoEliminarUsuario(usuario):
    contador = 0 

    saldo = consultarSaldo(usuario[0]) # Se consulta el saldo del usuario y con la estructura de decisión siguiente se verifica que el saldo no sea cero
    if float(saldo) > 0 :
        print("La cuenta aún tiene saldo disponible, por favor vuelve a jugar o retira el dinero.")
        return "0"
    else:

        op = ""
        while len(op) < 6 :
            op = getpass.getpass("Ingrese el pin del usuario: ") # Se le solicita el pin a usuario y se verifica que tenga las características necesarias
        if len(op) < 6 :
            print("Por favor, ingrese un pin con 6 caracteres o mas")
            contador += 1 
        else:
            if usuario[1] == op:
                validaUsuario = 1 # el pin se compara con el que se tiene almacenado para este usuario, si es así se le asigna 1 a la variable "validaUsuario"
            else:
                validaUsuario = 0
            if validaUsuario == 0:
                contador += 1 
                print("PIN incorrecto por favor reintente nuevamente")
        if contador == 3 :
            print("Se excedió el máximo de intentos para ingresar su PIN, volviendo al menú principal")
            return
        
        if validaUsuario == 1:
            print(f"Se procedera a eliminar el usuario {usuario[0]}.")
            time.sleep(1.5)
            for i in range(1, 6): # este ciclo imprime 5 puntos cada 1.5 segundos, lo cual da la impresión de tiempo de espera
                print(".", end=' ')
                time.sleep(1.5)
            print()
            eliminaUsuario(usuario) # EN el caso de que la validación haya sido positiva (validaUsuario == 1) entonces se llama a la función "eliminaUsuario" (que está más adelante)
            return "1"
        else:
            print("No se ha realizado la autenticación correctamente, por favor intente de nuevo!")
            return "2"

def eliminaUsuario(usuario):

    directorio_a_eliminar = os.path.abspath(os.path.join(os.getcwd(), "..", usuario[0]))

    if os.path.exists(directorio_a_eliminar) and os.path.isdir(directorio_a_eliminar): # Se verifica si la carpeta con la información del usuario existe
        try:
            shutil.rmtree(directorio_a_eliminar) # "shutil.rmtree" es un método que permite eliminar la carpeta y todos sus contenidos

            nombreArchivo = "usuarios_pines.txt"

            carpetaActual = os.path.abspath(os.path.dirname(__file__))

            rutaArchivo = os.path.join(carpetaActual, "..", nombreArchivo)

            lstUsuarios = consultarUsuarios() # Con las líneas anteriores se busca actualizar el archivo de usuarios


            usuariosNuevo = [] # Aquí se van a almacenar los datos de los usuarios que no se van a eliminar

            for usuarioBusqueda in lstUsuarios:
                if usuarioBusqueda[0] != usuario[0]:
                    usuariosNuevo.append(usuarioBusqueda) # Se agregan los usuarios que no se van a eliminar a la lista

            rutaArchivo = os.path.join(carpetaActual, "..", nombreArchivo)
            with open(rutaArchivo, "w") as archivo:
                if len(usuariosNuevo) == 0:
                    archivo.writelines(str(pinConfigAvanzada))
                else:
                    archivo.writelines(str(pinConfigAvanzada)+"\n")

            with open(rutaArchivo, "a") as archivo:
                for escribirLinea in usuariosNuevo:
                        linea = "\n".join(escribirLinea)
                        archivo.write(str(linea)) # Se agregan los usuarios que no se eliminan al archivo

            print(f"Usuario {usuario[0]} eliminado correctamente.")

        except OSError as e:
            print(f"Error al eliminar la carpeta {usuario[0]}: {e}")
    else:
        print(f"La carpeta del usuario {usuario[0]} no existe o no es una carpeta válida.")

def menuConfigAvanzada():
    opcion = ""

    while opcion != "4":
        cargaConfigAvanzada()
        print("1. Eliminar usuario")
        print("2. Modificar valores del sistema")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listaUsuario = consultarUsuarios() #Se llama a la función "consultarUsuarios" para obtener la lista de usuarios
            validaUsuario = 0
            contador = 0 
            usrList = [] # Lista vacía para almacenar la información del usuario

            if len(listaUsuario)>0:
                op = ""
                while len(op) < 5 :
                    op = input("Ingrese el usuario a eliminar: ")
                    if len(op) < 5 :
                        print("Por favor, ingrese un usuario con 5 caracteres o mas")
                        contador += 1 
                    else:
                        for fila in listaUsuario: #si el usuario existe en la lista de usuarios, se almacenan los detalles del usuario en "usrList" y "validaUsuario" se establece en 1
                            if fila[0] == op:
                                usrList.append(fila[0])
                                usrList.append(fila[1])
                                validaUsuario = 1
                                break
                            
                        if validaUsuario == 0:
                            contador += 1 
                            print("Usuario no existe por favor reintente nuevamente")
                    if contador == 3 :
                        print("Se excedió el máximo de intentos para ingresar su usuario, volviendo al menú principal")
                        return
                    else:
                        print("No hay usuarios registrados en el sistema")

                if validaUsuario == 1:
                    print(f"Se procedera a eliminar el usuario {usrList[0]}.")
                    time.sleep(1.5)
                    for i in range(1, 6):
                        print(".", end=' ')
                        time.sleep(1.5)
                    print()
                    eliminaUsuario(usrList) # Se llama a la función "eliminarUsuario", que elimina el usuario
            else:
                print("No hay usuarios registrados en el sistema.")

        elif opcion == "2":
            modificarValConfig() # Se llama a la función "modificarValConfig" que está adelante en este código
        elif opcion == "3":
            print("")
            break
        else:
            print("Por favor, seleccione una opción válida.")

# La siguiente función nos permite modificar los valores de la configuración avanzada
def modificarValConfig():
    opcion = ""

    while opcion != "4": # El ciclo while que se ejecuta hasta que decida salir
        cargaConfigAvanzada()
        print("¿Qué desea modificar?")
        print("1. Tipo de cambio: Compra de dólares usando colones")
        print("2. Tipo de cambio: Compra de dólares usando bitcoins")
        print("3. Valor acumulado Tragamonedas")
        print("4. Apuesta mínima Tragamonedas")
        print("5. Apuesta mínima Blackjack")
        print("6. Inversión mínima para registrarse")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        # Esta estructura de decisión permite modificar los valores de tipo de cambio y puestas mínimas dependiendo de a opción que escoja el usuario
        if opcion == "1":
            print(f"Valor actual del tipo de cambio Compra de dólares usando colones: {configAvanzada[0]}")
            tipoCambio = float(input("Ingresa el nuevo tipo de cambio:"))
            if tipoCambio<=0:
                print("El valor del tipo de cambio no puede ser igual o menor a 0")
            else:
                modificarConfigAvanzada(tipoCambio, 1)
                print(f"El valor del tipo de cambio Compra de dólares usando colones ha sido modificado el nuevo valor es de: {tipoCambio}\n")
        elif opcion == "2":
            print(f"Valor actual del tipo de cambio Compra de dólares usando bitcoins: {configAvanzada[1]}")
            tipoCambio = float(input("Ingresa el nuevo tipo de cambio:"))
            if tipoCambio<=0:
                print("El valor del tipo de cambio no puede ser igual o menor a 0")
            else:
                modificarConfigAvanzada(tipoCambio, 2)
                print(f"El valor del tipo de cambio Compra de dólares usando bitcoins ha sido modificado el nuevo valor es de: {tipoCambio}\n")
        elif opcion == "3":
            print(f"Valor actual acumulado del Tragamonedas: {configAvanzada[2]}")
            valorTragamonedas = float(input("Ingresa el nuevo valor acumulado del Tragamonedas:"))
            if valorTragamonedas<0:
                print("El valor del acumulado del tragamonedas no puede ser menor a 0")
            else:
                modificarConfigAvanzada(valorTragamonedas, 3)
                print(f"El valor del acumulado del tragamonedas ha sido modificado el nuevo valor es de: {valorTragamonedas}\n")
        elif opcion == "4":
            print(f"Valor actual de la apuesta mínima del Tragamonedas: {configAvanzada[3]}")
            valorTragamonedas = float(input("Ingresa el nuevo valor de apuesta mínima del Tragamonedas:"))
            if valorTragamonedas<1:
                print("El valor de apuesta mínima del tragamonedas no puede ser menor a 1")
            else:
                modificarConfigAvanzada(valorTragamonedas, 4)
                print(f"El valor de apuesta mínima del tragamonedas ha sido modificado el nuevo valor es de: {valorTragamonedas}\n")
        elif opcion == "5":
            print(f"Valor actual de la apuesta mínima del Blackjack: {configAvanzada[4]}")
            valorBlackjack = float(input("Ingresa el nuevo valor de apuesta mínima del Blackjack:"))
            if valorBlackjack<1:
                print("El valor de apuesta mínima del Blackjack no puede ser menor a 1")
            else:
                modificarConfigAvanzada(valorBlackjack, 4)
                print(f"El valor de apuesta mínima del Blackjack ha sido modificado el nuevo valor es de: {valorBlackjack}\n")
        elif opcion == "6":
            print(f"Valor actual de la inversión mínima para registrarse: {configAvanzada[5]}")
            inversionMinima = float(input("Ingresa el nuevo valor de inversión mínima para registrarse:"))
            if inversionMinima<0:
                print("El valor de registro mínimo no puede ser menor a 0")
            else:
                modificarConfigAvanzada(inversionMinima, 5)
                print(f"El valor de registro mínimo ha sido modificado el nuevo valor es de: {inversionMinima}\n")
        elif opcion == "7":
            break
        else:
            print("Por favor, seleccione una opción válida.")
    return

opcion = ""

while opcion != "4":
    cargaConfigAvanzada()
    consultarUsuarios()
    print("Bienvenido al menú:")
    print("1. Registro de usuario nuevo")
    print("2. DreamWorld Casino")
    print("3. Configuración Avanzada")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registroUsuario()
    elif opcion == "2":
        dreamWorldCasino()
    elif opcion == "3":
        contador = 0
        while True:
            op = ""
            while len(op) < 6 :
                op = getpass.getpass("Ingrese el pin especial: ")
            if len(op) < 6 :
                print("Por favor, ingrese un pin con 6 caracteres o mas")
                contador += 1 
            else:
                if pinConfigAvanzada == op:
                    validaUsuario = 1
                    break
                else:
                    validaUsuario = 0
                if validaUsuario == 0:
                    contador += 1 
                    print("PIN incorrecto por favor reintente nuevamente")
            if contador == 3 :
                print("Se excedió el máximo de intentos para ingresar el PIN, volviendo al menú principal")
                break
            
        if validaUsuario == 1:
            menuConfigAvanzada()
    elif opcion == "4":
        print("Gracias por participar")
    else:
        print("Por favor, seleccione una opción válida.")

