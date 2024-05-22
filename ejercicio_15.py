#Crea un algoritmo para la sucesión de Fibonacci. La sucesión de Fibonacci es la siguiente serie:
 #0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
#Pista: Empezando por 0 y 1, el siguiente número es la suma de los dos números últimos.
limite=12
anterior=0
actual=1
siguiente=actual #2 #3 #5
for n in range (12):
    print(siguiente, end=", ")
    #end lo pone en horizontal.
    anterior=actual
    actual=siguiente
    siguiente=anterior+actual
    
