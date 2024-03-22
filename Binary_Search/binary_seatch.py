def busca_binaria(array, valor):

  esquerda = 0
  direita = len(array) - 1

  while esquerda <= direita:
    meio = (esquerda + direita) // 2

    if array[meio] == valor:
      return meio
    elif array[meio] < valor:
      esquerda = meio + 1
    else:
      direita = meio - 1

  return -1

# Exemplo de uso
array = [1, 3, 5, 7, 9]
valor = 5

indice = busca_binaria(array, valor)

if indice == -1:
  print("O valor não foi encontrado no array.")
else:
  print(f"O valor foi encontrado no índice {indice}.")
