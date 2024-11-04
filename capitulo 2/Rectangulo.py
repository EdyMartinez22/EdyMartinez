class Rectangulo:
    def __init__(self, largo, ancho):
        self.__ancho = ancho
        self.__largo = largo

    def getarea(self):
        return self.__largo * self.__ancho

    def perimetro(self):
        return 2 * (self.__ancho + self.__largo)

    def largo(self):
        return self.__largo

    def getmaxlargo(rect1, rect2):

        if rect1.largo() == rect2.largo():
            return "Son iguales"
        elif rect1.largo() > rect2.largo():
            return "El rectangulo 1 es mas largo"
        else:
            return "El rectangulo 2 es mas largo"

rect1 = Rectangulo(2,8)
rect2 = Rectangulo(4,10)
Rectangulo.getmaxlargo(rect1, rect2)