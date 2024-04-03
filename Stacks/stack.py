
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, element):
        self.items.append(element)
    
    def pop(self):
        if self.items == 0:
            return None
        else:
            print(f"O elemento '{self.items.pop()}' foi remevido da pilha.")
    
    def size(self):
        print(f"A pilha contém:  {len(self.items)} elementos.")
    
    def peek(self): 
        print(f"Elemento no topo da pilha: {self.items[-1]}")
    

# Instancia a classe
myStack = Stack()

# Verifica o tamanho da Pilha
myStack.size()

# Adiciona elementos à pilha
myStack.push("Page One")
myStack.push("Page Two")
myStack.push("Page three")

# Remove elementos da pilha
myStack.pop() # remove o elemento do topo

# Verifica novamente a quantidade de ele. da pilha
myStack.size()

# Exibe o elemento do topo da pilha
myStack.peek()