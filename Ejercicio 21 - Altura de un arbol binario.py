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
                
    def altura(self):
        return self.calcular_altura(self.raiz)
    
    def calcular_altura(self, nodo):
        if nodo is None:
            return 0
        else:
            altura_izquierda = self.calcular_altura(nodo.izquierda)
            altura_derecha = self.calcular_altura(nodo.derecha)
            
            return 1 + max(altura_izquierda, altura_derecha)
        
        
        
arbol = ArbolBinario()

arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(2)
arbol.insertar(4)
arbol.insertar(6)
arbol.insertar(8)

print(f"Altura del arbol: {arbol.altura()}")