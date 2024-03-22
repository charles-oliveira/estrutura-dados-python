

def left_rotation(a, d):
    return a[d:] + a[:d]

a = [1, 2, 3, 4, 5]
print(left_rotation(a, 2))