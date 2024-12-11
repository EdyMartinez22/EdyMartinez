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
                
    def recorrer_inorden(self):
        valores = []
        self.recorrer_inorden_recursivo(self.raiz, valores)
        return valores
    
    def recorrer_inorden_recursivo(self, nodo, valores):
        if nodo:
            self.recorrer_inorden_recursivo(nodo.izquierda, valores)
            valores.append(nodo.dato)
            self.recorrer_inorden_recursivo(nodo.derecha, valores)
            
    def buscar(self, dato):
        return self.buscar_recursivo(self.raiz, dato)
    
    def buscar_recursivo(self, nodo, dato):
        if nodo is None:
            return False
        if nodo.dato == dato:
            return True
        elif dato < nodo.dato:
            return self.buscar_recursivo(nodo.izquierda, dato)
        else:
            return self.buscar_recursivo(nodo.derecha, dato)
        
        
        
arbol = ArbolBinario()

arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(2)
arbol.insertar(4)
arbol.insertar(6)
arbol.insertar(8)

print(f"Recorrido en orden: {arbol.recorrer_inorden()}")

print(f"Buscar 4: {arbol.buscar(4)}")
print(f"Buscar 9: {arbol.buscar(9)}")