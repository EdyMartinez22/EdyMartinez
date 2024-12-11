def duplicados(lista):
    if not lista:
        print("La lista esta vacia")
        return []
    
    nueva_lista = []
    for i in lista:
        if i not in nueva_lista:
            nueva_lista.append(i)
    return nueva_lista

lista = [5,2,6,9,7,7,8,8,10,10]
lista_sin_duplicados = duplicados(lista)

print(f"Lista original: {lista}")
print(f"Lista sin duplicados: {lista_sin_duplicados}")
