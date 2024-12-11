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
            
    def eliminar_duplicados(self):
        if not self.cabeza:
            return

        valores_vistos = set()
        actual = self.cabeza
        previo = None
        
        while actual:
            if actual.dato in valores_vistos:
                previo.siguiente = actual.siguiente
            else:
                valores_vistos.add(actual.dato)
                previo = actual
            actual = actual.siguiente
            
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
lista.agregar_al_final(10)
lista.agregar_al_final(30)
lista.agregar_al_final(20)

print("Lista original:")
lista.mostrar()

lista.eliminar_duplicados()

print("Lista despues de eliminar duplicados:")
lista.mostrar()