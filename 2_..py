from funciones import limpiar_pantalla
limpiar_pantalla()

# 2- LLenar una lista de 10 posiciones con números aleatorios entre 1 y 100, como 
# salida debe mostrar los números aleatorios del arreglo ordenados de menor a mayor. 
# me guie con los siguientes link:
# https://www.freecodecamp.org/espanol/news/python-tutorial-de-lista-vacia-como-crear-y-comprobar-una-lista-vacia-en-python/
# https://www.freecodecamp.org/espanol/news/ordenar-listas-en-python-como-ordenar-por-descendente-o-ascendente/


numeros_aleatorios = [] # Inicializamos la lista vacia

#luego la llenamos con valores: 
for x in range(1,11):
    agregar= int(input(f"{x}- Agregue un numero a la lista: ")) # creamos una variable donde agregaremos valores
    numeros_aleatorios.append(agregar) #usamos la función "append" que va agregando valores al final de la lista

print(f"lista actualizada: {numeros_aleatorios}")
numeros_aleatorios.sort() # acá ordenamos la lista con ".sort()"
print(f"lista ordenada de menor a mayor: {numeros_aleatorios}") # y acá la imprimimos ya ordenada
