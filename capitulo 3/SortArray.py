class Array(object):
    def __init__(self, initialSize):
        """Constructor: Inicializa un array con el tamaño especificado."""
        self.__a = [None] * initialSize  # El array almacenado como lista
        self.__nItems = 0  # No hay elementos en el array inicialmente

    def __len__(self):
        """Devuelve el número de elementos en el array."""
        return self.__nItems

    def get(self, n):
        """Devuelve el valor en el índice n, si está dentro de los límites."""
        if 0 <= n < self.__nItems:  # Verifica si n está dentro de los límites
            return self.__a[n]

    def set(self, n, value):
        """Establece el valor en el índice n, si está dentro de los límites."""
        if 0 <= n < self.__nItems:  # Verifica si n está dentro de los límites
            self.__a[n] = value

    def swap(self, j, k):
        """Intercambia los valores en los índices j y k."""
        if (0 <= j < self.__nItems and  # Verifica si los índices están dentro de los límites
                0 <= k < self.__nItems):
            self.__a[j], self.__a[k] = self.__a[k], self.__a[j]

    def insert(self, item):
        """Inserta un elemento al final del array."""
        if self.__nItems >= len(self.__a):  # Si el array está lleno
            raise Exception("Array overflow")  # Lanza una excepción
        self.__a[self.__nItems] = item  # El elemento va al final actual
        self.__nItems += 1  # Incrementa el número de elementos

    def find(self, item):
        """Busca el índice del elemento especificado."""
        for j in range(self.__nItems):   # Entre los elementos actuales
            if self.__a[j] == item:       # Si se encuentra el elemento
                return j                   # Retorna el índice del elemento
        return -1                        # No encontrado -> devuelve -1

    def search(self, item):
        """Busca un elemento en el array y lo devuelve si lo encuentra."""
        return self.get(self.find(item))  # Busca el elemento y devuelve si se encuentra

    def delete(self, item):
        """Elimina la primera ocurrencia del elemento especificado."""
        for j in range(self.__nItems):   # Entre los elementos actuales
            if self.__a[j] == item:       # Si se encuentra el elemento
                self.__nItems -= 1         # Uno menos al final
                for k in range(j, self.__nItems):  # Mueve los elementos a la izquierda
                    self.__a[k] = self.__a[k + 1]
                return True                # Devuelve un indicador de éxito

        return False  # Si se llega aquí, no se pudo encontrar el elemento

    def traverse(self, function=print):
        """Recorre todos los elementos y aplica una función a cada uno."""
        for j in range(self.__nItems):
            function(self.__a[j])

    def __str__(self):
        """Devuelve una representación en cadena del array."""
        ans = "["  # Inicia la cadena con un corchete izquierdo
        for i in range(self.__nItems):
            if len(ans) > 1:  # Si ya hay elementos en la cadena
                ans += ", "  # Separa los elementos con una coma
            ans += str(self.__a[i])  # Agrega la representación en cadena del elemento
        ans += "]"  # Cierra con un corchete derecho
        return ans

    def bubbleSort(self):
        """Ordena el array usando el algoritmo de burbuja."""
        for last in range(self.__nItems - 1, 0, -1):  # Bucle que recorre los elementos
            for inner in range(last):  # El bucle interno va hasta el último no ordenado
                if self.__a[inner] > self.__a[inner + 1]:  # Si el elemento es mayor que el siguiente
                    self.swap(inner, inner + 1)  # Intercambia los elementos

    def selectionSort(self):
        """Ordena el array seleccionando el mínimo y colocándolo en la posición más a la izquierda."""
        for outer in range(self.__nItems - 1):  # Asume que el mínimo está a la izquierda
            min_index = outer  # El mínimo asumido es el más a la izquierda
            for inner in range(outer + 1, self.__nItems):  # Busca a la derecha
                if self.__a[inner] < self.__a[min_index]:  # Si se encuentra un nuevo mínimo
                    min_index = inner  # Actualiza el índice del mínimo
            self.swap(outer, min_index)  # Intercambia el mínimo encontrado con el izquierdo

    def insertionSort(self):
        copias = 0
        comparaciones = 0

        """Ordena el array usando inserciones repetidas."""
        for outer in range(1, self.__nItems):  # Marca un elemento
            temp = self.__a[outer]  # Almacena el elemento marcado en temp
            inner = outer  # El bucle interno empieza en el marcado
            while inner > 0 and temp < self.__a[inner - 1]:  # Si el elemento marcado es menor
                comparaciones += 1
                if temp < self.__a[inner - 1]:
                    copias += 1
                    self.__a[inner] = self.__a[inner - 1]  # Desplaza el elemento hacia la derecha
                    inner -= 1  # Mueve el índice interno hacia la izquierda
                else:
                    break #si no hay mas comparaciones
            self.__a[inner] = temp  # Coloca el elemento marcado en la posición correcta
            copias += 1
        print(f"Numero de copias: {copias} y comparaciones: {comparaciones}")

    # ejercicio 3.2
    def getmedia(self):
        pos = (self.__nItems // 2)
        if self.__nItems % 2 != 0:
            return self.__a[pos]
        else:
            media1 = self.__a[pos]
            media2 = self.__a[pos - 1]
            return (media1 + media2) / 2

    #ejercicio 3.3
    def deduplicate(self):
        if self.__nItems <= 1:
            return [] # si el array tiene 0 o 1 elemento, no hay elementos a eliminar

        duplicados = [] #todos los elementos duplicados
        pos_elements = 0 #elementos unicos

        for i in range(1, self.__nItems):
            if self.__a[i] == self.__a[pos_elements]:
                duplicados.append(self.__a[i]) #agrega el elemento duplicado
            else:
                pos_elements += 1
                self.__a[pos_elements] = self.__a[i]

        return duplicados

    def oddEvenSort(self):
        n = self.__nItems
        intercambios =  False #saber si se han hecho intercambios
        pasadas = 0 #contar cuantas pasadas

        while not intercambios:
            intercambios = True #si esta ordenado

            for j in range(1, n - 1, 2): #primer pasada
                if self.__a[j] > self.__a[j+1]:
                    self.swap(j,j+1)
                    intercambios = False #ha hecho intercambios

            for j in range(0,n - 1, 2): #segunda pasada
                if self.__a[j] > self.__a[j+1]:
                    self.__a[j], self.__a[j+1] = self.__a[j+1], self.__a[j]
                    intercambios = False

            pasadas += 1
        return pasadas

    def clear(self, capacidad = 10): #vaciar la lista para probar otras funciones
        self.__a = [None] * capacidad
        self.__nItems = 0
