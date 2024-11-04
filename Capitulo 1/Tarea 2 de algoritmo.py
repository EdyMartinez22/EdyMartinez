cadena = "4 and 20 blackbirds."

lista = [caracter for caracter in cadena]
print("Caracteres:",lista)

lista_sin_espacios = [caracter for caracter in cadena if caracter != ' ']
print("Sin espacios:", lista_sin_espacios)