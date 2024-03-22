class Pilha:
    # constructor
    def __init__(self):
        self.pilha = []

    # function or method to put something on the top 
    def push(self, item):
        self.pilha.append(item)

    def pop(self):
        self.pilha.pop()
    
    def is_empty(self):
        if len(self.pilha) == 0:
            print('Sua pilha está vazia')
        else:
            print('sua lista contém elemento(s)')
    
    def peek(self):
        if not self.is_empty():
            return self.pilha[-1] # Access last element
        else:
            return None


