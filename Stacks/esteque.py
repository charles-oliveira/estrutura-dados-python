
class Stack:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)
    
    def pop(self):
        if self.size() == 0:
            print("Não há elementos para ser retirado da pilha.")
        else:
            self.items.pop()
    
    
    def size(self):
        print(f"O tamanho da pilha {len(self.items)}")
    

myStack = Stack()

myStack.push("page number 1")
myStack.push("page number 2")
myStack.push("page number 3")
print(myStack.items)
myStack.pop()
