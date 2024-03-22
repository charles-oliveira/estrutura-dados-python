""""
push - adds an item to the top of the stack
pop - removes an item from the top of the stack (and returns the value of that item)
size - returns the size of the stack

"""


class Stack:
    def __init__(self):
        self.items = []

    # push an item to the top of the items 
    def push(self, element):
        self.items.append(element)

    def pop(self):
        if self.size() == 0:
            print("Não é possível remover itens da pilha, pois está vazia.")
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)

myStack = Stack()

myStack.push("Page 1")
myStack.push("Page 2")
myStack.push("Page 3")
myStack.push("Page 4")

print(myStack.items)

myStack.pop()
print(myStack.items)


print(myStack.size())


























# print(str(myStack.size()))
# myStack.push(1)
# myStack.push(4)
# myStack.push(9)
# print(f"O item removido da pilha foi: {myStack.pop()}")
# print(f"A quantidade de item ou itens que restam na pilha: {myStack.size()}")
# print("------------")

# myStack.pop()
# myStack.pop()
# myStack.pop()






    
    
