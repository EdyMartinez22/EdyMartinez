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
    
def balanceada(cadena):
    pila = Pila()
    pares = {')': '(', '}':'{', ']':'['}
    
    for i in cadena:
        if i in '({[': 
            pila.push(i)
        elif i in ')}]':
            if pila.vacio() or pila.pop() != pares[i]:
                return False
    return pila.vacio()

if __name__ == "__main__":
    cadenas = [
        "()", 
        "{[()()]}",
        "({[()]})",
        "({[()()]})",
        "(()",
        "({[)}",
        "((()))",
        "({[({})]})"
    ]
    
    for cadena in cadenas:
        print(f"La cadena '{cadena}' esta balanceada? {balanceada(cadena)}")
    
