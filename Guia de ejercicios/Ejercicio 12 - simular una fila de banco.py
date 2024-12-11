class Cliente:
    def __init__(self, numero):
        self.numero = numero
        
    def __str__(self):
        return f"Cliente {self.numero}"
    
class ColaBanco:
    def __init__(self):
        self.cola = []
        
    def agregar_cliente(self, numero_cliente):
        cliente = Cliente(numero_cliente)
        self.cola.append(cliente)
        print(f"{cliente} agregado a la cola")
        
    def atender_cliente(self):
        if not self.vacio():
            cliente = self.cola.pop(0)
            print(f"Atendiendo a {cliente}")
            return cliente
        else:
            print("No hay clientes en la cola")
            return None
        
    def mostrar_proximo_cliente(self):
        if not self.vacio():
            print(f"Proximo cliente a atender: {self.cola[0]}")
        else:
            print("No hay clientes en la cola")
            
    def vacio(self):
        return len(self.cola) == 0
    
    def mostrar_cola(self):
        if not self.vacio():
            print("Clientes en espera: ")
            for cliente in self.cola:
                print(cliente)
        else:
             print("No hay clientes en la cola")  
             
             
banco = ColaBanco()

banco.agregar_cliente(1)
banco.agregar_cliente(2)
banco.agregar_cliente(3)

banco.mostrar_proximo_cliente()

banco.atender_cliente()
banco.atender_cliente()

banco.mostrar_proximo_cliente()

banco.mostrar_cola()

banco.atender_cliente()

banco.atender_cliente()