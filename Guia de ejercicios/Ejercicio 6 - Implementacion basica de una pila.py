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

if __name__ == "__main__":
    pila = Pila()
    print(f"Estado inicial de la pila: {pila}")
    
    
pila.push(5)
pila.push(12)
pila.push(40)
pila.push(36)
pila.push(11)
print(f"La pila agregandoles elementos: {pila}")

print(f"numero del final de la pila: {pila.peek()}")

print(f"Eliminar elemento: {pila.pop()}")
print(f"La pila despues de eliminar un elemento: {pila}")