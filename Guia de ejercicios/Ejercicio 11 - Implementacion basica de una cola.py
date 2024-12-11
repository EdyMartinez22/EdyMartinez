class Cola:
    def __init__(self):
        self.cola = []
    
    def enqueue(self, elemento):
        self.cola.append(elemento)
        print(f"Elemento {elemento} agregado a la cola")
        
    def dequeue(self):
        if not self.vacio():
            elemento = self.cola.pop(0)
            print(f"Elemento {elemento} eliminado de la cola")
            return elemento
        else:
            print("La cola esta vacia")
            return None
        
    def peek(self):
        if not self.vacio():
            return self.cola[0]
        else:
            print("La cola esta vacia")
            return None
        
    def vacio(self):
        return len(self.cola) == 0
    
    def mostrar_cola(self):
        print(f"Cola actual: {self.cola}")
    

cola = Cola()

cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)

print(f"Primer elemento (peek): {cola.peek()}")

cola.dequeue()

print(f"Primer elemento (peel) despues de dequeue: {cola.peek()}")

cola.mostrar_cola()