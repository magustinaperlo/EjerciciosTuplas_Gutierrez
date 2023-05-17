#Crea una tupla con números, pide al usuario un número por teclado e indica cuantas veces se
#repite según lo halle en la tupla que has creado.

#RESUELVE validar los ingresos del usuario.
numeros = (1, 2, 2, 3, 4, 9, 7, 6, 3, 2, 6, 6, 2, 3, 4, 2, 4, 6, 4, 6, 3, 7 ,6, 7, 8, 9, 10, 11, 1, 10, 10)


while True:
    num = int(input("Ingrese numero: "))
    print(numeros.count(num))    
