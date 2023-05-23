#Crea una tupla con valores ya predefinidos del 1 al 10, pide al usuario un índice por teclado y
#muestra los valores de la tupla.

#RESUELVE el caso en que no exista ese índice en la tupla.

tupla_numeros = ()
indice = 0

tupla_numeros = (1,2,3,4,5,6,7,8,9,10)
while True:

    indice = int(input("Ingrese un indice: "))
    
    if indice >= 0 and indice < len(tupla_numeros):
        print(tupla_numeros[indice]) 
    else:
        print("Indice no valido")
        
   #sugerencia 

tupla_numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

while True:
    indice = int(input("Ingrese un índice (-1 para salir): "))
    
    if indice == -1:
        break
    
    if 0 <= indice < len(tupla_numeros):
        print(tupla_numeros[indice])
    else:
        print("Índice no válido")


