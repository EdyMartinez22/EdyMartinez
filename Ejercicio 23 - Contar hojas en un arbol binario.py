class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None
        
class ArbolBinario:
    def __init__(self):
        self.raiz = None
        
    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = NodoArbol(dato)
        else:
            self.insertar_recursivo(self.raiz, dato)
            
    def insertar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(dato)
            else:
                self.insertar_recursivo(nodo.izquierda, dato)
        elif dato > nodo.dato:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(dato)
            else:
                self.insertar_recursivo(nodo.derecha, dato)

    def contar_hojas(self):
        return self.contar_hojas_recursivo(self.raiz)
    
    def contar_hojas_recursivo(self, nodo):
        if nodo is None:
            return 0
        
        if nodo.izquierda is None and nodo.derecha is None:
            return 1
        
        return self.contar_hojas_recursivo(nodo.izquierda) + self.contar_hojas_recursivo(nodo.derecha)
    


arbol = ArbolBinario()

arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(2)
arbol.insertar(4)
arbol.insertar(6)
arbol.insertar(8)


print(f"Numero de nodos hoja: {arbol.contar_hojas()}")