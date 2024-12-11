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
                
    def recorrer_por_niveles(self):
        if not self.raiz:
            return []
        
        resultado = []
        cola = [self.raiz]
        
        while cola:
            nodo = cola.pop(0)
            resultado.append(nodo.dato)
            
            if nodo.izquierda:
                cola.append(nodo.izquierda)
            if nodo.derecha:
                cola.append(nodo.derecha)
                
        return resultado
    
    
arbol = ArbolBinario()

arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(2)
arbol.insertar(4)
arbol.insertar(6)
arbol.insertar(8)
    
print(f"Recorrido por niveles: {arbol.recorrer_por_niveles()}")