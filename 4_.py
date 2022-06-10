# Dado una lista de 100 elementos numéricos enteros (1 al 100),
# generar el código que muestre todos los números de la lista 
# y la suma de ella
from funciones import limpiar_pantalla
limpiar_pantalla()

numeros = []
for x in range(1,101): #cambiar a un numero más pequeño para comprobar más rápido xd
    sw = True
    while sw == True:
        ingresar_numero = int(input(f"{x}: Ingrese un numero: "))
        if ingresar_numero >0 and ingresar_numero <=100:
            numeros.append(ingresar_numero)
            sw = False
        else:
            print("Ingrese sólo numeros entre el 1 y el 100 porfis")
print(numeros)
suma = 0
for x in numeros:
    suma = suma + x
print(f"La suma de los números ingresados es: {suma}")

#for x in numeros:
#   print(x) # esto es si quisieramos mostrar el listado hacía abajo