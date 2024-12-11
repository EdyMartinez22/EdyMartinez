class Cola:
    def __init__(self):
        self.cola = []
        
    def enqueue(self, elemento):
        self.cola.append(elemento)
        
    def dequeue(self):
        if not self.vacia():
            return self.cola.pop(0)
        else:
            print("La cola esta vacia")
            return None
        
    def vacia(self):
        return len(self.cola) == 0
    
    def peek(self):
        if not self.vacia():
            return self.cola[0]
        else:
            print("La cola esta vacia")
            return None
    
    def tamano(self):
        return len(self.cola)
    
    def ordenar(self):
        n = self.tamano()
        for i in range(n):
            for j in range(n - 1):
                primer = self.dequeue()
                segundo = self.dequeue()
                
                if primer > segundo:
                    self.enqueue(segundo)
                    self.enqueue(primer)
                else: 
                    self.enqueue(primer)
                    self.enqueue(segundo)
                    
            for k in range (i):
                self.enqueue(self.dequeue())
                
    def mostrar_cola(self):
        print(f"Cola actual: {self.cola}")
        

cola_numeros = Cola()

numeros = [3,8,5,9,1,6,4,6,4]
for i in numeros:
    cola_numeros.enqueue(i)
    
print("Cola original: ")
cola_numeros.mostrar_cola()

cola_numeros.ordenar()

print("Cola ordenada:")
cola_numeros.mostrar_cola()