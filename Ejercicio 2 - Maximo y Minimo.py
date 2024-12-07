lista = [55,9,8,15,62]
print(f"La lista es de: {lista}")

valor_max = lista[0] #Se inician las variables con el primer numero de la lista
valor_min = lista[0]

for i in lista:
    if i > valor_max:
        valor_max = i
    if i < valor_min:
        valor_min = i
        
print(f"El valor maximo es de: {valor_max}")
print(f"El valor minimo es de: {valor_min}")