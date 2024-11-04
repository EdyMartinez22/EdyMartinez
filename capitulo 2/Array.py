class Array(object):

    def __init__(self, capacidad = 100): # Constructor
        self.__a = [None] * capacidad # The array stored as a list
        self.__nItems = 0 # No items in array initially

    def __len__(self): # Special def for len() func
        return self.__nItems # Return number of items

    def get(self, n): # Return the value at indexn
        if 0 <= n and n < self.__nItems: # Check if n is in bounds, and
            return self.__a[n] # only return item if in bounds

    def set(self, n, value): # Set the value at index n
        if 0 <= n and n < self.__nItems: # Check if n is in bounds, and
            self.__a[n] = value # only set item if in bounds

    def insert(self, items): # Insert item at end
        self.__a[self.__nItems] = items # Item goes at current end
        self.__nItems += 1 # Increment number of items

    def push(self, item):
        self.__a[self.__nItems] = item
        self.__nItems += 1

    def pop(self):
        if self.__nItems == 0:
            return None
        item = self.__a[self.__nItems - 1]
        self.__a[self.__nItems - 1] = None
        self.__nItems -= 1
        return item

    def find(self, item): # Find index for item
        for j in range(self.__nItems): # Among current items
            if self.__a[j] == item: # If found,
                return j # then return index to item
        return -1 # Not found -> return -1

    def search(self, item): # Search for item
        return self.get(self.find(item)) # and return item if found

    def delete(self, item): # Delete first occurrence
        for j in range(self.__nItems): # of an item
            if self.__a[j] == item: # Found item
                self.__nItems -= 1 # One fewer at end
                for k in range(j, self.__nItems): # Move items from
                    self.__a[k] = self.__a[k+1] # right over 1
                return True # Return success flag
        return False # Made it here, so couldn't find the item

    def traverse(self, function=print): # Traverse all items
        for j in range(self.__nItems): # and apply a function
            function(self.__a[j])

    # ejercicio 2.1
    def getMaxNum(self): #buscar numero maximo
        MaxNum = None
        for i in range(self.__nItems):
            if isinstance(self.__a[i],(int,float)):
                if MaxNum is None or self.__a[i] > MaxNum: 
                    MaxNum = self.__a[i] 
        return MaxNum

    #ejercicio 2.2
    def deleteMaxNum(self): #borrar de la lista el numero maximo

        MaxNum = self.getMaxNum()
        for i in range(self.__nItems):
            if self.__a[i] == MaxNum:
                self.__nItems -= 1
                for k in range(i,self.__nItems):
                    self.__a[k] = self.__a[k+1]
                return True
        return False
    
    def getpromedio(self):
        suma = 0
        cuenta = 0
        for i in range(self.__nItems):
            if isinstance(self.__a[i],(int,float)):
                suma += self.__a[i]
                cuenta += 1
        if cuenta > 0:
            return suma / cuenta
        return None
    
    def cuenta(self, tipo):
        pares=impares= 0
        for i in range(self.__nItems):
            if isinstance(self.__a[i], (int,float)):
                if self.__a[i] % 2 == 0:
                    pares += 1
                else:
                    impares += 1
        if tipo == 0:
            return impares
        if tipo == 1:
            return pares
        
    def palabras(self):
        palabras = []
        for i in range(len(self.__a)):
            if isinstance(self.__a[i],str):
                palabras.append(self.__a[i])
        return palabras

    #ejercicio 2.4
    def removeDupes(self):
        items_unicos = []
        for item in self.__a:
            if item not in items_unicos:
                items_unicos.append(item)
        self.__a = items_unicos
        self.__nItems = len(items_unicos)