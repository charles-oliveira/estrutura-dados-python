
class Fila:
    def __init__(self):
        self._fila = []
    
    def enfileirar(self, elemento):
        self._fila.append(elemento)

    def desenfileirar(self):
        if self._fila == 0:
            print("Não há elementos na fila.")
        else:
            print(f"O elemento: {self._fila.pop(0)} foi desenfileirado")
    
    def esta_vazia(self):
        return not self._fila
    
    def tamanho_fila(self):
        print(f"O tamando da fila: {len(self._fila)}")



# criando uma instancia
fila = Fila()



fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)

fila.tamanho_fila()

# desenfileirando dois elementos, portanto, deve restar o terceiro ele.
fila.desenfileirar()
fila.desenfileirar()

fila.tamanho_fila()
