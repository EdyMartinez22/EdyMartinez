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
    
    def reorganizar_pares_impares(self):
        pares = []
        impares = []
        
        while not self.vacia():
            elemento = self.dequeue()
            if elemento % 2 == 0:
                pares.append(elemento)
            else:
                impares.append(elemento)
                
        self.cola = pares + impares
        
    def mostrar_cola(self):
        print(f"Cola actual: {self.cola}")
        
    
cola_numeros = Cola()

numeros = [1,2,3,4,5,6]
for i in numeros:
    cola_numeros.enqueue(i)
    
cola_numeros.mostrar_cola()

cola_numeros.reorganizar_pares_impares()

print("Cola reorganizada (pares al principio, impares al final):")
cola_numeros.mostrar_cola()