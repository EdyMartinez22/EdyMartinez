import Pila
import Cola

print("-----Menu-----")
print("1. Pila")
print("2. Cola")
print("3. Salir")
n = int(input("Elija una opcion(1-3): "))

if n == 1:
    print("-----Pila-----")
    pila = Pila.Pila()
    pila.pila()
elif n == 2:
    print("-----Cola-----")
    cola = Cola.Cola()
    cola.cola()
elif n == 3:
    exit()
else:
    print("Opcion invalida.")