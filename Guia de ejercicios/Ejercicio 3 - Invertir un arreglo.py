def orden_inverso(elementos):
    lista =[]
    
    for i in range(len(elementos) - 1, -1, -1):
        lista.append(elementos[i])
    return lista

lista = [1,2,3,5,8,9,15]
print(f"La lista es: {lista}")
ordeninverso = orden_inverso(lista)

print(f"Lista invertida: {ordeninverso}")