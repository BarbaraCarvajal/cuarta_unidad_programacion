# 5- Desarrollar un algoritmo que a partir de una lista lst = [1,2,3,4,5]
# genere una segunda lista lst2 con los valores lst2 =[1,3,6,10,15]

from funciones import limpiar_pantalla
limpiar_pantalla()

lista = [1,2,3,4,5]
lista2 = [1,3,6,10,15]


a = (lista[0])
b = (lista[0]+lista[1])
c = (lista[0]+lista[1]+lista[2])
d = (lista[0]+lista[1]+lista[2]+lista[3])
e = (lista[0]+lista[1]+lista[2]+lista[3]+lista[4])
suma = a,b,c,d,e
print(suma)

for x in lista:
    x = x + lista[0]
    x = x + 1
    print(x)