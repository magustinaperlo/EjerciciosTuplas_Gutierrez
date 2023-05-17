#Crea una tupla con números e indica el numero con mayor valor y el que menor tenga.

Numeros = (1,19,24,50,2,-3,4,5,17,32,290,-2,-35)
mayor= Numeros[0]
menor= Numeros[0]


for i in Numeros:
    if (i>mayor):
        mayor= i
    if (i<menor):
        menor= i


print("El mayor es: ", mayor, "\nEl menor es: ", menor)
    