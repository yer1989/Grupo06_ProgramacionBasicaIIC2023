#Proyecto Introduccion a la programacion 
#Autor Grupo 6 
#Problema Crear un programa que tenga un menu con 4 opciones para un casino crear un usuario y registrar, se debe solicitar al usuario 
#que desea realizar

import getpass 

#Variables
listausuario = []
listacontrasena = []
listanombre = []
listadivisa = []


def registrousuario() :
    op = ""
    contador = 0
    while len(op) < 5 :
        op = input("Ingrese su nombre su usuario: ")
        if len(op) < 5 :
            print("Por favor, ingrese un usuario con 5 caracteres o mas")
            contador += 1 
        else:
            listausuario.append(op)
        if contador == 3 :
            print("Ha alcanzado el limite de intentos")
            return
    
    op = input("Ingrese su nombre:")
    listanombre.append(op)

    op = ""
    while len(op) < 6 :
        op= getpass.getpass("Ingrese su contraseña: ")
        if len(op) < 6 :
            print("Por favor, ingrese una contraseña de 6 caracteres o mas")
        else:
            listacontrasena.append(op)
    monto = 0 
    op = ""
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
                op = float(input("Ingrese un monto a depositar en su cuenta: "))
                contador += 1 
                monto = op

            elif divisa == 2:
                print("2.Colones")
                op = float(input("Ingrese un monto a depositar en su cuenta: "))
                contador += 1 
                monto = op / 538

            elif divisa == 3:
                print("3.Bitcoin")
                op = float(input("Ingrese un monto a depositar en su cuenta: "))
                contador += 1 
                monto = op * 26755

            else: 
                print("Por favor, seleccione una opcion valida")

            if contador == 3:
                print("Limite alcanzado en el deposito, por favor vuelva a iniciar")
                listacontrasena.pop()
                listanombre.pop()
                listausuario.pop()
                return
    listadivisa.append(monto)

    print("Transaccion realizada satisfactoriamente, su saldo es de: "+str(monto)+" dolares ")


opcion = ""

while opcion != "4":
    print("Bienvenido al menú:")
    print("1. Registro de usuario nuevo")
    print("2. DreamWorld Casino")
    print("3. Configuración Avanzada")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrousuario()
    elif opcion == "2":
        print("dreamworldcasino()")
    elif opcion == "3":
        print("configuracionavanzada()")
    elif opcion == "4":
        print("Gracias por participar")
    else:
        print("Por favor, seleccione una opción válida.")
