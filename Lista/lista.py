
def busca(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return None

lista_sonhada = [42, 'Charles', 8, 2024, 'Sucesso']
elemento_procurado = 'Sucesso'


indice = busca(lista_sonhada, elemento_procurado)
if indice is not None:
    print("O índice do elemento {} é {}".format(elemento_procurado, indice))
else:
    print("O elemento {} não se encontra na lista.".format(elemento_procurado))
