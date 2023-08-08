#Proyecto Introduccion a la programacion 
#Autor Grupo 6 


#Se importan las librerías que permiten crear un password; crear y leer archivos (entre otras operaciones con archivos); crear números aleatorios y funciones relacionadas con el tiempo
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

#Estos paréntesis sirven para hacer una definición
usuario = {
    "usuario": "",
    "contrasena": "",
    "nombreusuario":"",
    "dinerocuenta": ""
}

configAvanzada = []
pinConfigAvanzada = ""

def cargaConfigAvanzada():

#Creamos el archivo en el que vamos a introduccir la información
    
    nombreArchivo = "configuracion_avanzada.txt"

    carpetaPadre = os.path.abspath(os.path.dirname(__file__))

    rutaArchivo = os.path.join(carpetaPadre, "..", nombreArchivo)
    global configAvanzada
    try:
        with open(rutaArchivo, 'r') as archivo:
            configAvanzada = archivo.readlines()
        
    except FileNotFoundError:
        print("No se pudo encontrar el archivo: {}".format(nombreArchivo))
    except IOError:
        print("Error al leer el archivo: {}".format(nombreArchivo))

def crearUsuario(usuario) : 
    try:
        nombreCarpeta = str(usuario["usuario"])

        carpetaPadre = os.path.join(os.getcwd(), os.pardir, nombreCarpeta)

        if not os.path.exists(carpetaPadre):
            os.makedirs(carpetaPadre)
        else:
            return 0

        nombreArchivo = "saldos.txt"

        rutaArchivo = os.path.join(carpetaPadre, nombreArchivo)

        with open(rutaArchivo, "w") as archivo:
            archivo.write(str(round(float(usuario["dinerocuenta"]),2)))

        nombreArchivo = "usuarios_pines.txt"

        carpetaActual = os.path.abspath(os.path.dirname(__file__))

        rutaArchivo = os.path.join(carpetaActual, "..", nombreArchivo)
        with open(rutaArchivo, "a") as archivo:
            archivo.write("\n" + str(usuario["usuario"]) + "\n" + str(usuario["contrasena"] + "\n" +str(usuario["nombreusuario"])))

        return 1
    except Exception as e:
        return 0

def registroUsuario() :
    op = ""
    contador = 0
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

    op = ""
    
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

    op = ""
    
    while len(op.strip()) == 0 :
        op= input("Ingrese su nombre: ")
        if len(op.strip()) == 0 :
            print("Por favor, ingrese un nombre, el campo no puede quedar vacio.")
        else:
            usuario["nombreusuario"] = op

    monto = 0 
    op = ""
    contador = 0
    while monto < int(configAvanzada[5].strip()):
            divisa = ""

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
    usuario["dinerocuenta"] = monto

    if crearUsuario(usuario) == 1 :
        print(f"Transaccion realizada satisfactoriamente, su saldo es de: ${str(monto)}.")
    else :
        print("Error al guardar el usuario.")

def dreamWorldCasino():
    listaUsuario = consultarUsuarios()
    validaUsuario = 0
    contador = 0 
    usrList = []

    if len(listaUsuario)>0:
        op = ""
        while len(op) < 5 :
            op = input("Ingrese su usuario: ")
        if len(op) < 5 :
            print("Por favor, ingrese un usuario con 5 caracteres o mas")
            contador += 1 
        else:
            for fila in listaUsuario:
                if fila[0] == op:
                    usrList.append(fila[0])
                    usrList.append(fila[1])
                    usrList.append(fila[2])
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

    contador = 0 
    if validaUsuario == 1:
        op = ""
        while len(op) < 6 :
            op = getpass.getpass("Ingrese el pin del usuario: ")
        if len(op) < 6 :
            print("Por favor, ingrese un pin con 6 caracteres o mas")
            contador += 1 
        else:
            if usrList[1] == op:
                validaUsuario = 1
            else:
                validaUsuario = 0
            if validaUsuario == 0:
                contador += 1 
                print("PIN incorrecto por favor reintente nuevamente")
        if contador == 3 :
            print("Se excedió el máximo de intentos para ingresar su PIN, volviendo al menú principal")
            return
    
    if validaUsuario == 1:
        print("Bienvenido " + usrList[0] + " a DreamWorld Casino!")
        opcion = ""

        while opcion != "6":

            saldo = consultarSaldo(usrList[0])
            if saldo == "error":
                print("Se ha presentado un error obteniendo el saldo.")
                break
            elif len(usrList) == 3 :
                usrList.append(float(saldo))
            else:
                usrList[3] = float(saldo)

            print("1. Retirar dinero")
            print("2. Depositar dinero")
            print("3. Ver saldo actual")
            print("4. Juegos en línea")
            print("5. Eliminar usuario")
            print("6. Salir")

            opcion = input("Seleccione una opción: ")

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
                    
                    print("1. Blackjack")
                    print("2. Tragamonedas")
                    print("3. Salir")

                    opcJuego = input("Seleccione una opción: ")
                    if opcJuego == "1":
                        print("Reglas juegoBlackJack")
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
    nombreArchivo = os.path.join(os.pardir, usuario, "saldos.txt")

    def obtenerUltimoRegistro(archivo):
        with open(archivo, "r") as archivo_txt:
            lineas = archivo_txt.readlines()
            if lineas:
                return lineas[-1]
            else:
                return None

    saldo = obtenerUltimoRegistro(nombreArchivo)

    if saldo:
        return saldo.strip() 
    else:
        return "error"

def consultarUsuarios():
    nombreArchivo = "usuarios_pines.txt"

    carpetaActual = os.path.abspath(os.path.dirname(__file__))

    rutaArchivo = os.path.join(carpetaActual, "..", nombreArchivo)
    try:
        with open(rutaArchivo, 'r') as archivo:
            usuarios = archivo.readlines()

        global pinConfigAvanzada 
        pinConfigAvanzada = str(usuarios[0].strip())

        del usuarios[0]

        listaUsuario = []
        for linea in range(0, len(usuarios), 3):
            usuario = usuarios[linea].strip()
            contrasena = usuarios[linea + 1].strip()
            nombreUsuario = usuarios[linea + 2].strip()
            listaUsuario.append([usuario, contrasena, nombreUsuario])

        return listaUsuario
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo: {nombreArchivo}")
    except IOError:
        print(f"Error al leer el archivo: {nombreArchivo}")


def retirarDinero(usuario):
    op = ""
    contador = 0
    bandera = True
    print(f"{usuario[2]} tu saldo actual es de: {str(usuario[3])}.")
    while bandera :
        op = input("¿Cuanto desea retirar?: ")
        if float(op) == 0 or float(op) > float(usuario[3]) or float(op) < 0:
            print("Por favor, ingrese un monto correcto.")
            contador += 1 
        else:
            usuario[3] = float(usuario[3]) - float(op)
            actualizarSaldo(usuario)
            print(f"Su retiro de dinero ha sido exitoso, su saldo actual es de: {str(usuario[3])}.")
            bandera = False

        if contador == 3 :
            print("Se excedió el máximo de intentos para realizar su retiro de dinero, volviendo al menú principal.")
            bandera = False
    return 0

def depositarDinero(usuario):

    divisa = ""
    monto = 0

    print("Realice su deposito")
    print("1. Dolares")
    print("2. Colones")
    print("3. Bitcoin")

    divisa = int(input("Seleccione una divisa: "))

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
    actualizarSaldo(usuario)
    print(f"Su deposito de dinero ha sido exitoso, {usuario[2]} su saldo actual es de: {str(usuario[3])}.")

def actualizarSaldo(usuario):
    nombreArchivo = "saldos.txt"

    nombreArchivo = os.path.join(os.pardir, usuario[0], "saldos.txt")

    rutaArchivo = os.path.join(nombreArchivo, "..", nombreArchivo)
    with open(rutaArchivo, "a") as archivo:
        archivo.write("\n" + str(round(usuario[3],2)))
    return 

def juegoBlackJack(usuario):

    saldo = float(usuario[3])
    apuestaMinima = float(configAvanzada[4].strip())

    while saldo >= apuestaMinima and True:
        apuesta = float(input(f"{usuario[2]} tu saldo es {saldo}. ¿Cuánto deseas apostar? (mínimo {apuestaMinima}): "))
        if apuesta < apuestaMinima:
            print("Apuesta insuficiente. Debes apostar al menos el mínimo.")
            continue

        # Reparto inicial de cartas
        jugadorCartas = [generarCarta(), generarCarta()]
        crupierCartas = [generarCarta(), generarCarta()]

        mostrarCartasJugador(jugadorCartas)

        print(f"La primera carta del crupier es: {crupierCartas[0]}")
        
        if puedeDividir(jugadorCartas):
            opcion = input("¿Deseas doblar tu apuesta 1 o dividir la jugada 2? ").upper()
        else:
            opcion = input("¿Deseas doblar tu apuesta 1? ").upper()

        if opcion == '1':
            if saldo >= apuesta * 2:
                apuesta *= 2
                print(f"Apostaste el doble: {apuesta}")
            else:
                print("Saldo insuficiente para doblar la apuesta.")

        if puedeDividir(jugadorCartas):
            jugadorCartas, cartasJuego2, saldo = dividirJugada(jugadorCartas, saldo, apuesta)
            saldo = jugarRonda(jugadorCartas, crupierCartas, apuesta, saldo)
            mostrarCartasJugador(cartasJuego2)
            saldo = jugarRonda(cartasJuego2, crupierCartas, apuesta, saldo)
        else:
            saldo = jugarRonda(jugadorCartas, crupierCartas, apuesta, saldo)
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
    if len(cartas) != 2 or cartas[0].split()[0] != cartas[1].split()[0]:
        print("No puedes dividir la jugada en este momento.")
        return cartas, saldo

    if saldo < apuesta:
        print("Saldo insuficiente para dividir la jugada.")
        return cartas, saldo

    nuevaCarta1 = generarCarta()
    nuevaCarta2 = generarCarta()

    print("Dividiendo la jugada...")
    print(f"Juego 1: {cartas[0]} y {nuevaCarta1}")
    print(f"Juego 2: {cartas[1]} y {nuevaCarta2}")

    cartasJuego1 = [cartas[0], nuevaCarta1]
    cartasJuego2 = [cartas[1], nuevaCarta2]

    return cartasJuego1, cartasJuego2, saldo - apuesta

def jugarRonda(jugadorCartas, crupierCartas, apuesta, saldo):
    while True:
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
        elif accion == '2':
            break
        else:
            print("Opción no válida. Ingresa 1 para pedir una nueva carta o 2 para detener el juego.")

    if valorMano(jugadorCartas) <= 21:
        print("Turno del crupier...")
        print(f"La carta oculta del crupier es: {crupierCartas[1]}")
        while valorMano(crupierCartas) < 17:
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

    print(f"Tu saldo actual es: {saldo}")
    return saldo


def mostrarMaquinaTragamonedas(figuras):
    print("Este es el resultado")
    time.sleep(1.5)
    for figura in figuras:
        print(figura, end=' ')
        time.sleep(1.5)
    print()

def jugarMaquinaTragamonedas(usuario):
    saldoActual = usuario[3]
    apuestaMinima = float(configAvanzada[3].strip())
    cantidadJugadas = 1
    acumulado = float(configAvanzada[2].strip())

    while True:
        apuesta = float(input(f"{usuario[2]} cuanto desea apostar? Tu saldo es de: {saldoActual}: "))
        if saldoActual < apuestaMinima:
            print("No tienes suficiente dinero para jugar.")
            return
        if apuesta < apuestaMinima:
            print("El monto a apostar es menor a la apuesta mínima.")
        else:
            saldoActual -= apuesta

            print(f"Saldo actual: {saldoActual}")
            input("Presione Enter para jalar la palanca e iniciar el juego.")

            figuras = [random.choice(["@", "#", "+", "7"]) for _ in range(3)]

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
                resultadoFigura = [random.choice(figuras) for _ in range(3)]

            mostrarMaquinaTragamonedas(resultadoFigura)

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
            
            usuario[3] = saldoActual
            actualizarSaldo(usuario)
            modificarConfigAvanzada(str(acumulado),3)
            cargaConfigAvanzada()

        print(f"{usuario[2]} tu saldo actual es de: {saldoActual}")
        jugarNuevamente = input("¿Deseas jugar nuevamente? (1 Sí o 2 No): ")
        if jugarNuevamente != '1':
            break


def modificarConfigAvanzada(linea, numeroLinea):
    nombreArchivo = "configuracion_avanzada.txt"

    carpetaActual = os.path.abspath(os.path.dirname(__file__))

    rutaArchivo = os.path.join(carpetaActual, "..", nombreArchivo)

    with open(rutaArchivo, 'r') as f:
        lineas = f.readlines()

    lineas[numeroLinea - 1] = str(linea) + '\n'

    with open(rutaArchivo, 'w') as f:
        f.writelines(lineas)
    return


def procesoEliminarUsuario(usuario):
    contador = 0 

    saldo = consultarSaldo(usuario[0])
    if float(saldo) > 0 :
        print("La cuenta aún tiene saldo disponible, por favor vuelve a jugar o retira el dinero.")
        return "0"
    else:

        op = ""
        while len(op) < 6 :
            op = getpass.getpass("Ingrese el pin del usuario: ")
        if len(op) < 6 :
            print("Por favor, ingrese un pin con 6 caracteres o mas")
            contador += 1 
        else:
            if usuario[1] == op:
                validaUsuario = 1
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
            for i in range(1, 6):
                print(".", end=' ')
                time.sleep(1.5)
            print()
            eliminaUsuario(usuario)
            return "1"
        else:
            print("No se ha realizado la autenticación correctamente, por favor intente de nuevo!")
            return "2"

def eliminaUsuario(usuario):

    directorio_a_eliminar = os.path.abspath(os.path.join(os.getcwd(), "..", usuario[0]))

    if os.path.exists(directorio_a_eliminar) and os.path.isdir(directorio_a_eliminar):
        try:
            shutil.rmtree(directorio_a_eliminar)

            nombreArchivo = "usuarios_pines.txt"

            carpetaActual = os.path.abspath(os.path.dirname(__file__))

            rutaArchivo = os.path.join(carpetaActual, "..", nombreArchivo)

            lstUsuarios = consultarUsuarios()


            usuariosNuevo = []

            for usuarioBusqueda in lstUsuarios:
                if usuarioBusqueda[0] != usuario[0]:
                    usuariosNuevo.append(usuarioBusqueda)

            rutaArchivo = os.path.join(carpetaActual, "..", nombreArchivo)
            with open(rutaArchivo, "w") as archivo:
                if len(usuariosNuevo) == 0:
                    archivo.writelines(str(pinConfigAvanzada))
                else:
                    archivo.writelines(str(pinConfigAvanzada)+"\n")

            with open(rutaArchivo, "a") as archivo:
                for escribirLinea in usuariosNuevo:
                        linea = "\n".join(escribirLinea)
                        archivo.write(str(linea))

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
            listaUsuario = consultarUsuarios()
            validaUsuario = 0
            contador = 0 
            usrList = []

            if len(listaUsuario)>0:
                op = ""
                while len(op) < 5 :
                    op = input("Ingrese el usuario a eliminar: ")
                    if len(op) < 5 :
                        print("Por favor, ingrese un usuario con 5 caracteres o mas")
                        contador += 1 
                    else:
                        for fila in listaUsuario:
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
                    eliminaUsuario(usrList)
            else:
                print("No hay usuarios registrados en el sistema.")

        elif opcion == "2":
            modificarValConfig()
        elif opcion == "3":
            print("")
            break
        else:
            print("Por favor, seleccione una opción válida.")

def modificarValConfig():
    opcion = ""

    while opcion != "4":
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
