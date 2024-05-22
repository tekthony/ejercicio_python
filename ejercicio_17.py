#Crea un programa en Python que simule el funcionamiento de un cajero automático. El programa debe permitir al usuario realizar las siguientes operaciones:

# Verificar el saldo de su cuenta.
# Depositar dinero en su cuenta.
# Retirar dinero de su cuenta.
# Salir del programa.
# El programa debe iniciar con un saldo inicial predeterminado y mostrar un menú con las siguientes opciones:

# Verificar saldo
# Depositar dinero
# Retirar dinero
# Salir

saldo:int=100
mensaje=f"""
_________________MENU DE OPCIONES_________________
1.Verificar saldo
2.Depositar dinero
3.Retirar dinero
4.Salir
"""

while True:
    print(mensaje)
    opcion=input("Ingreser la accion que desea realizar: ")
    if opcion == "1":
        print(f"el saldo en su cuenta es de: {saldo}")
    elif opcion == "2":
        cantidad=int(input("ingresa la cantidad a suma: "))
        print(f"se agrego {cantidad} asu saldo actual de {saldo}")
        saldo+=cantidad
    elif opcion == "3":
        cantidad=int(input("ingresa la cantidad a retira: "))
        print(f"se retiro {cantidad} as u saldo de {saldo}")
        saldo-=cantidad
    elif opcion == "4":
        break