def outer_func(a,b):
    square = a **2, b**2
    def addition(a,b):
        return a + b
    add = addition(a,b)
    return add + 5
result = outer_func(3,11)
print(result)