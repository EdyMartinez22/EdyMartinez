class CalculadoraconPila:
    def __init__(self):
        self.pila = []
        
    def calcular(self, operaciones):
        for i in operaciones:
            if isinstance(i,(int,float)):
                self.pila.append(i)
            elif i in ['+','-','*','/']:
                n2 = self.pila.pop()
                n1 = self.pila.pop()
            
                if i == '+':
                    self.pila.append(n1 + n2)
                elif i == '-':
                    self.pila.append(n1 - n2)
                elif i == '*':
                    self.pila.append(n1 * n2)
                elif i == '/':
                    if n2 != 0:
                        self.pila.append(n1 / n2)
                    else:
                        return "Error: Division por cero"
        return self.pila[-1]
    
calculo = CalculadoraconPila()
operaciones = [2, 9, '+', 6, '*', 9, '-']
resultado = calculo.calcular(operaciones)
print(f"Resultado: {resultado}")