# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automatica el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 puede entrar gratis, si tiene entre 4 y 18 debe pagar 5 soles,
# y si es mayor de 18 deberá pagar 10 soles.

cliente:int=int(input("ingrese su edad: "))
if cliente < 4:
    print("entra gratis")
elif cliente <=18:
    print("total a pagar S/.5")
elif cliente >18:
    print("total a pagar S/.10")