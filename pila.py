

class nodoPila():
    info, sig = None, None


class Pila():

    def __init__(self):
        self.__tamanio = 0
        self.__cima = None

    def tamanio(self):
        return self.__tamanio
    
    def apilar(self, dato):
        nodo = nodoPila()
        nodo.info = dato
        nodo.sig = self.__cima
        self.__cima = nodo
        self.__tamanio += 1

    def cima(self):
        return self.__cima.info, self.__cima.sig


pila1 = Pila()  
pila1.apilar(1)
pila1.apilar(5)
print(pila1.cima())
print(pila1.tamanio())

print()