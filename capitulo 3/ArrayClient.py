import Array2

maxSize = 20 # Max size of the array
arr = Array2.Array2(maxSize)# Create an array object
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

#ejercicio 3.1
arr.bubbleSort()
print("Lista ordenada: ")
arr.traverse()
