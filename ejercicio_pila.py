
from pila import Pila
from random import randint

pila1 = Pila()

for i in range(15):
    num = randint(1, 5)
    print(num)
    pila1.apilar(num)

x = int(input('ingrese el numero que desae contar ocurrencias '))

contador = 0
while(not pila1.pila_vacia()):
    dato = pila1.desapilar()

    if(dato == x):
        contador += 1

print('cantidad de ocurrencias:', contador)
