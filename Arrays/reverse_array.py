"""
Task: Reverter um array

Exemplo: 

Input = [1, 4, 7, 9]
Output = [9, 7, 4, 1]

"""

def reverseArray_1(a):
    b = []
    for i in a:
        b.insert(0, i)
    return b

def reverseArray_02(a):
    return a[:: -1]

def reverseArray_03(a):
    a = a.reverse()
    return a


a = [1, 5, 8, 7]
print(f"Array original: {a}")
print("----------------------")
print(reverseArray_1(a))
print(reverseArray_02(a))
reverseArray_03(a)
print(a)
print("----------------------")

reverseArray_03(a)
print(f"Verificando o problema de usar a função reverse: {a}")