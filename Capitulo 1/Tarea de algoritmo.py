import random

#Cartas
lista = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
valor_letras = {'A':1, 'J':11, 'Q':12, 'K':13}
random.shuffle(lista)
espadas = '♠'
carta = [f"{l}{espadas}" for l in lista]
print(f'Lista desordenada: {carta}')

#Identificar si el elemento es letra o numero
def obtener_valor(elemento):
    if isinstance(elemento, str):
        return valor_letras.get(elemento, 0)
    return elemento

#Ordenamiento de las cartas
for i in range(len(lista)):
    for j in range(len(lista)-1):
        if obtener_valor(lista[j]) > obtener_valor(lista[j+1]):
            lista[j], lista[j + 1] = lista[j+1], lista[j]

#Cartas ya ordenadas
carta_ordenada = [f"{l}{espadas}" for l in lista]
print(f"Lista ordenada: {carta_ordenada}")