# 3- Almacene nombres en una lista de n posiciones. Una vez completada
# la lista, implementar una opción que al ingresar una posición
# muestre el dato que contiene. 

from funciones import  limpiar_pantalla
limpiar_pantalla()

nombres = []

pregunta = int(input("¿Cuántos nombres ingresará?: "))
for x in range(1,pregunta+1):
    agregar = input(f"{x}: Ingrese un nombre: ")
    nombres.append(agregar)
    #print(nombres) #para comprobar que se agregaron bien los nombres

posicion = int(input("Ingrese la posición que desea ver: "))
print(f"En la posición {posicion} esta: {nombres[posicion]}")
# dentro de los corchetes lo que hicimos fue lo mismo que por ejemplo poner:
# nombres[1] 1 seria la posición que queremos mostrar, en este caso dicha 
# posición la estamos consultando por teclado. 

