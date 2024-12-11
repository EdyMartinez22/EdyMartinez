class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cola = [None] * capacidad
        self.frente = 0
        self.final = -1
        self.tamano = 0
        
    def enqueue(self, elemento):
        if self.llena():
            print("Error: La cola esta llena.")
            return
        self.final = (self.final + 1) % self.capacidad
        self.cola[self.final] = elemento
        self.tamano += 1
        print(f"Elemento {elemento} añadiendo a la cola")
    
    def dequeue(self):
        if self.vacia():
            print("Error: La cola esta vacia")
            return None
        elemento = self.cola[self.frente]
        self.cola[self.frente] = None
        self.frente = (self.frente + 1) % self.capacidad
        self.tamano -= 1
        print(f"Elemento {elemento} eliminado de la cola")
        return elemento
    
    def peek(self):
        if self.vacia():
            print("La cola esta vacia")
            return None
        return self.cola[self.frente]
    
    def vacia(self):
        return self.tamano == 0
    
    def llena(self):
        return self.tamano == self.capacidad
    
    def mostrar_cola(self):
        print(f"Cola: {self.cola}, Frente: {self.frente}, Final: {self.final}, Tamaño: {self.tamano}")
        
        
cola_circular = ColaCircular(5)

cola_circular.enqueue(10)
cola_circular.enqueue(20)
cola_circular.enqueue(30)
cola_circular.enqueue(40)
cola_circular.enqueue(50)

cola_circular.enqueue(60)

cola_circular.mostrar_cola()

cola_circular.dequeue()
cola_circular.dequeue()

cola_circular.mostrar_cola()

cola_circular.enqueue(60)
cola_circular.enqueue(70)

cola_circular.mostrar_cola()