import Array
import random

class Pila(object):
    def pila(self):

        maxSize = 100
        arr = Array.Array(maxSize)

        for i in range(100):
            arr.push(random.randint(0,300))

        arr.traverse()

        sumapar=sumaimpar=cuentapar=cuentaimpar=promediopar=promedioimpar = 0
        for i in range(100):
            numberPop = arr.pop()
            if numberPop is not None:
                if numberPop % 2 == 0:
                    sumapar += i
                    cuentapar += 1
                    promediopar = sumapar / cuentapar
                else:
                    sumaimpar += i
                    cuentaimpar += 1
                    promedioimpar = sumaimpar / cuentaimpar

        print(f"La suma par es de: {sumapar}, la cantidad de numeros: {cuentapar} y el promedio: {promediopar}")
        print(f"La suma impar es de: {sumaimpar}, la cantidad de numeros: {cuentaimpar} y el promedio: {promedioimpar}")