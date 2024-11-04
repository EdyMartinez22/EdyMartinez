from Rectangulo import Rectangulo
from Rectangulo import rect1, rect2

#medidad ya dadas
print(f"Area del rectangulo 1 es: {Rectangulo.getarea(rect1)}")
print(f"Area del rectangulo 2 es: {Rectangulo.getarea(rect2)}")
print(f"El perimetro del rectangulo 1 es: {Rectangulo.perimetro(rect1)}")
print(f"El perimetro del rectangulo 2 es: {Rectangulo.perimetro(rect2)}")
print(Rectangulo.getmaxlargo(rect1,rect2)) #Triangulo mas alto
print("")

#Ingresar otras medidas
print("---Calcular otros rectangulos---")
largo = float(input("Ingrese el largo: "))
ancho = float(input("Ingrese el ancho: "))
rect_usuario = Rectangulo(largo, ancho)
print(f"El area es: {rect_usuario.getarea()}")
print(f"El perimetro es: {rect_usuario.perimetro()}")