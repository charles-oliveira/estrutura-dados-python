def busca_binaria(array, item):

    comeco = 0
    fim = len(array) - 1

    while comeco <= fim:
        meio = (comeco + fim) // 2

        if array[meio] == item:
            return meio
        elif array[meio] < item: 
            comeco = meio + 1
        else:
            fim = meio - 1
    
    return None


array = [1, 3, 5, 7, 9]
valor = 5

indice = busca_binaria(array, valor)

if indice == -1:
  print("O valor não foi encontrado no array.")
else:
  print(f"O valor foi encontrado no índice {indice}.")
