def binary_search(array, item):
    """
    Realiza uma pesquisa binária em um array ordenado e retorna o índice do item
    ou None se não for encontrado. Também conta o número de comparações feitas.

    Argumentos:
        array: Lista ordenada de elementos.
        item: O valor a ser buscado no array.

    Retorna:
        O índice do item no array ou None se não for encontrado.
        A quantidade de comparações feitas durante a busca.
    """

    begin = 0
    end = len(array) - 1
    count = 0

    while begin <= end:
        count += 1
        m = (begin + end) // 2

        if array[m] == item:
            return m, count
        elif array[m] < item:
            begin = m + 1
        else:
            end = m - 1

    return None, count # retorna um par de valores

array = [i for i in range(1, 101)]   # list(range(1, 101))
item = 30

indice, comparacoes = binary_search(array, item)

if indice is not None:
    print(f"O valor foi encontrado no índice {indice} e precisou de {comparacoes} tentativas.")
else:
    print(f"O valor não foi encontrado após {comparacoes} tentativas.")
    
    
# A função retorna um par de valores: 
# o índice do item no array ou None se o item não for encontrado, 
# e o número de comparações feitas durante a busca.