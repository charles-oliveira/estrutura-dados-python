class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Fila:
    def __init__(self):
        self._primeiro = None
        self._ultimo = None
    
    def enfileirar(self, elemento):
        novo_no = No(elemento)
        if self._ultimo is not None:
            self._ultimo.proximo = novo_no
        self._ultimo = novo_no
        if self._primeiro is None:
            self._primeiro = novo_no
    
    