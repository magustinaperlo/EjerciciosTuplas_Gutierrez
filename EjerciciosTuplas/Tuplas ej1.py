#Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la
#longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de
#error.

#El programa termina cuando el usuario introduce un cero.

meses=("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
v=True

while v == True:

    print("Ingrese numero de mes: ")
    num = int(input())

    if (num<=12 and num != 0):
        print(meses[num-1])

    elif (num==0):
        v= False
    else:
        print("Error")

        
#sugerencia
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

while True:
    num = int(input("Ingrese el número de mes (0 para salir): "))

    if num == 0:
        break

    if 1 <= num <= len(meses):
        print(meses[num - 1])
    else:
        print("Error: Número de mes inválido")



