"""
Exemplo de como trabalhar com filas

queue = []
queue.insert(0, 127) # index 2
queue.insert(0, 128) # index 1
queue.insert(0, 227) # index 0
queue.pop()

"""

# from Stacks.stack import Stack


# class Queue:
#     def __init__(self):
#         self.instorage = Stack()
#         self.outstorage = Stack()
    
#     def size(self):
#         return self.instorage.size() + self.outstorage.size()
    
#     def enqueue(self, element):
#         self.instorage.push(element)
    
#     def dequeue(self):
#         if not self.outstorage.items:
#             while self.instorage.items:
#                 self.outstorage.push(self.instorage.pop())
#         return self.outstorage.pop()


# # create some tests to verify the implementation with pass and fail
    
# def test():
#     q = Queue()
#     q.enqueue(1)
#     q.enqueue(2)
#     q.enqueue(3)
#     assert q.size() == 3
#     assert q.dequeue() == 1
#     assert q.dequeue() == 2
#     assert q.dequeue() == 3
#     assert q.size() == 0
#     print('All test passed')

# test()



class Fila:
    def __init__(self):
        self.itens = []
        self.frente = 0  # Índice do primeiro elemento

    def tamanho(self):
        return len(self.itens) - self.frente

    def enfileirar(self, elemento):
        self.itens.append(elemento)

    def desenfileirar(self):
        if self.tamanho() == 0:
            raise ValueError("Fila vazia")
        elemento = self.itens[self.frente]
        self.frente += 1
        return elemento

    def esta_vazia(self):
        return self.tamanho() == 0



fila = Fila()

fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)

print(fila.tamanho())  # Saída: 3

elemento = fila.desenfileirar()
print(elemento)  # Saída: 1

elemento = fila.desenfileirar()
print(elemento)  # Saída: 2

fila.esta_vazia()  # Saída: False


