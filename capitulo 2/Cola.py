import Array
import random

class Cola(object):

    def cola(self):

        maxSize = 100
        arr = Array.Array(maxSize)

        for i in range(100):
            arr.insert(random.randint(0,300))

        arr.traverse()

        sumapar=sumaimpar=cuentapar=cuentaimpar=promediopar=promedioimpar = 0
        for i in range(100):
            numeros = arr.get(i)
            if numeros is not None:
                if numeros % 2 == 0:
                    sumapar += i
                    cuentapar += 1
                    promediopar = sumapar / cuentapar
                    arr.delete(0)
                elif numeros % 2 != 0:
                    sumaimpar += i
                    cuentaimpar += 1
                    promedioimpar = sumaimpar / cuentaimpar
                    arr.delete(0)

        print(f"La suma par es de: {sumapar}, la cantidad de numeros: {cuentapar} y el promedio: {promediopar}")
        print(f"La suma impar es de: {sumaimpar}, la cantidad de numeros: {cuentaimpar} y el promedio: {promedioimpar}")