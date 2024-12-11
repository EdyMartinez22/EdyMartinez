class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        
    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            
    def eliminar(self, dato):
        if not self.cabeza:
            print("La lista esta vacia.")
            return False
        
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            return True
        
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.dato != dato:
            actual = actual.siguiente
            
        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente
            return True
        
        else:
            print(f"El elemento {dato} no se encuentra en la lista")
            return False
        
    def buscar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False
    
    def mostrar(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        print(f"Lista: {elementos}")
        

lista = ListaEnlazada()

lista.agregar_al_final(10)
lista.agregar_al_final(20)
lista.agregar_al_final(30)

print("Lista despues de agregar elementos:")
lista.mostrar()

print(f"Esta el 20 en la lista? {lista.buscar(20)}")
print(f"Esta el 40 en la lista? {lista.buscar(40)}")

print("Eliminando el 20...")
lista.eliminar(20)
lista.mostrar()

print("Eliminando el 40...")
lista.eliminar(40)
lista.mostrar()