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
            
    def mostrar(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        print(f"Lista: {elementos}")
        
def combinar_listas_ordenadas(lista1, lista2):
    nueva_lista = ListaEnlazada()
    actual1 = lista1.cabeza
    actual2 = lista2.cabeza
    
    nodo_temporal = Nodo(None)
    actual_nueva = nodo_temporal
    
    while actual1 and actual2:
        if actual1.dato <= actual2.dato:
            actual_nueva.siguiente = actual1
            actual1 = actual1.siguiente
        else:
            actual_nueva.siguiente = actual2
            actual2 = actual2.siguiente
        actual_nueva = actual_nueva.siguiente
        
    actual_nueva.siguiente = actual1 if actual1 else actual2
    
    nueva_lista.cabeza = nodo_temporal.siguiente
    return nueva_lista

lista1 = ListaEnlazada()
lista1.agregar_al_final(1)
lista1.agregar_al_final(3)
lista1.agregar_al_final(5)

lista2 = ListaEnlazada()
lista2.agregar_al_final(2)
lista2.agregar_al_final(4)
lista2.agregar_al_final(6)

print("Lista 1:")
lista1.mostrar()

print("Lista 2: ")
lista2.mostrar()

lista_combinada = combinar_listas_ordenadas(lista1, lista2)
print("Lista combinada ordenada:")
lista_combinada.mostrar()