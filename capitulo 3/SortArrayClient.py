import SortArray

maxSize = 10 # Max size of the array
arr = SortArray.Array(maxSize)# Create an array object
arr.insert(77.40) # Insert 10 items
arr.insert(99)
arr.insert(40.51)
arr.insert(30.74)
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(12.34)
arr.insert(20.70)
arr.insert(9.7354)

#ejercicio 3.2
print(f"La media es: {arr.getmedia()}")

#ejercicio 3.3
duplicados = arr.deduplicate()
print("Numeros duplicados: ",duplicados)

#ejercicio 3.4
print(f"Numero de pasadas: {arr.oddEvenSort()}")
print("Lista ordenada con oddEvenSort: ")
arr.traverse()

print("Lista para el insertionSort")
arr.traverse()

arr.clear()

#ejercicio 3.5
print("Lista del insertSort:")
arr.insert(77.40) # Insert 10 items
arr.insert(99)
arr.insert(40.51)
arr.insert(30.74)
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(12.34)
arr.insert(20.70)
arr.insert(9.7354)
arr.traverse()
arr.insertionSort()
print("Lista ordenada: ")
arr.traverse()

#ejercicio 3.6

