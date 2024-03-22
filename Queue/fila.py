
class Fila:
    def __init__(self):
        self.fila = []

    def enqueue(self, item):
        self.fila.append(item)
    
    def dequeue(self):
        return self.fila.pop(0)
    
    def is_empty(self):
        return len(self.fila) == 0
    
    def peek(self):
        print(self.fila[-1])

    def showElements(self):
        print(self.fila)
    

fila = Fila()

fila.enqueue(1)
fila.enqueue(4)
fila.enqueue(6)
fila.showElements()
fila.dequeue()
fila.peek()
fila.is_empty()



