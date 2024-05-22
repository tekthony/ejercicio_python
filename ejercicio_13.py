#Vamos a diseñar una calculadora que se enciende y hasta que no tecleamos SAL no se apaga.

#Esta calculadora funciona de la siguiente manera:

#Recogemos los datos A y B
#"Si operación es 1 calcula la raíz cuadrada de la suma de A y B
#Si operación es 2 calcula A / B. Vigilamos que B no sea 0...
#Si la operación es 3 calculamos la siguiente fórmula: ( A * B ) / 2.5

while True:
    print(f"""
________MENU DE OPCIONES__________
    1.calcula la raiz cuadrada de la suma de A y B.
    2.calcula A/B.
    3.calcula (A*B)/2.5
    para salir escribe 'SAL'
        """)
    condicion=input("escribe CON o SAL:")
    if condicion.upper() == "SAL":
        break
    valor_A=int(input("ingrese el valor de A:"))
    valor_B=int(input("ingrese el valor de B:"))
    menu=input("Ingrese una opcion a realizar:")
    if menu=="1":
        suma=valor_A+valor_B
        print(f"la raiz de {suma} es: {pow(suma,2)}")
    elif menu=="2":
        while True:
            if valor_B == 0:
                valor_B=int(input("ingrese el valor de B:"))
            else:
                break
        divi=valor_A//valor_B
        print(f"la divicion es: {divi}")
    elif menu=="3":
        formula=(valor_A*valor_B)/2.5
        print(f"la formula es: {formula}")
        