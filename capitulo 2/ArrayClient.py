from array import array

import Array
maxSize = 100 # Max size of the array
from Array import *

arr = Array(maxSize) # Create an array object
arr.insert(77) # Insert 10 items
arr.insert(99)
arr.insert("foo")
arr.insert("bar")
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert("baz")
arr.insert(-17)

print("Array containing", len(arr), "items")
arr.traverse()
print("Search for 12 returns", arr.search(12))
print("Search for 12.34 returns", arr.search(12.34))
print("Deleting 0 returns", arr.delete(0))
print("Deleting 17 returns", arr.delete(17))
print("Setting item at index 3 to 33")
arr.set(3, 33)
print("Array after deletions has", len(arr), "items")
arr.traverse()
print(f"Los numeros pares son: {arr.cuenta(1)} y los impares son : {arr.cuenta(0)}")
print(f"El promedio es : {arr.getpromedio()}")
print(f"El numero maximo es: {arr.getMaxNum()}")
arr.delete(arr.getMaxNum())
print("La nueva lista: ")
arr.traverse()

#ejercicio 2.3
ordenar_numeros = []
while True:
    MaxNum = arr.getMaxNum()
    if MaxNum is not None:
        ordenar_numeros.insert(0,MaxNum)
        arr.delete(MaxNum)
    else:
        break
print(f"Lista ordenada: {ordenar_numeros}")
print(f"El numero de palabras es: {arr.palabras()}")

#ejercicio 2.4
arr.removeDupes()
print(f"Lista sin duplicados: {arr.traverse()}")
