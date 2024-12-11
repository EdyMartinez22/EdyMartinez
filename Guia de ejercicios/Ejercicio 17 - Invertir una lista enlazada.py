class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        
    def agregar_al_final(self,dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente =  nuevo_nodo
            
    def invertir(self):
        previo = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = previo
            previo = actual
            actual = siguiente
        self.cabeza = previo
        
    def mostrar(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        print(f"Lista: {elementos}")
        
    
lista = ListaEnlazada()

lista.agregar_al_final(1)
lista.agregar_al_final(2)
lista.agregar_al_final(3)
lista.agregar_al_final(4)

print("Lista original: ")
lista.mostrar()

lista.invertir()

print("Lista invertida:")
lista.mostrar()