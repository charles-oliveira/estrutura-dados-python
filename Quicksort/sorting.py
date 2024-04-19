def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quicksort(lista, inicio, p - 1)
        quicksort(lista, p + 1, fim)

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio  # seria "barra" amarela, ou seja, delimitando os núm. menrores
    for j in range(inicio, fim): # representa a "barra roxa"
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]  # faz a troca (swap) de valores
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i] 
    return i
    
array = [5, 2, 4, 6, 1, 3]
print(quicksort(array, 0, 5))


