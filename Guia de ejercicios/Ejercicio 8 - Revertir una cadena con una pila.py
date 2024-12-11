class Pila:
    def __init__(self):
        self.elementos = []
        
    def push(self, elemento):
        self.elementos.append(elemento)
    
    def pop(self):
        if self.vacio():
            raise IndexError("La lista esta vacia")
        return self.elementos.pop()
    
    def peek(self):
        if self.vacio():
            raise IndexError("La lista esta vacia")
        return self.elementos[-1]
    
    def vacio(self):
        return len(self.elementos) == 0
    
    def __str__(self):
        return str(self.elementos)
    
def invertir_cadena(cadena):
    pila = Pila()
    
    for i in cadena:
        pila.push(i)
        
    cadena_invertida = ""
    while not pila.vacio():
        cadena_invertida += pila.pop()
        
    return cadena_invertida

if __name__ == "__main__":
    texto = "Hola Mundo"
    texto_invertido = invertir_cadena(texto)
    print(f"Cadena original: {texto}")
    print(f"Cadena invertida: {texto_invertido}")