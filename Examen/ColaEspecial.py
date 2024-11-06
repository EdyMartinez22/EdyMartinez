class ColaEspecial:
    def __init__(self, max=15):
        self.__elem = [None] * max
        self.__pos = 0
    
    def __len__(self):
        return self.__elem
    
    def get(self, n):
        if 0 <= n < self.__pos:
            return self.__elem[n]

    def insert(self, valor):
        self.__elem[self.__pos] = valor
        self.__pos += 1

    def delete(self, valor):
        for i in range(self.__pos):
            if self.__elem[i] == valor:
                self.__pos -= 1
        
    def mostrar(self, pos=print):
        for i in range(self.__pos):
            pos(self.__elem[i])
    


    