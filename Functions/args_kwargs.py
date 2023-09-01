# *args, **kwargs

def super_func(*args): # stands for can have many arguments as needed
    print(args)
    return sum(args)

print(super_func(1, 2, 3, 4, 5))

# kwargs stands for keyword arguments
def super_func(*args, **kwargs):
    total = 0
    print(kwargs)
    for item in kwargs.values():
        total += item
    return sum(args) + total
    
print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))

# Rule: parameters, *args, default parameters, **kwargs

def super_func(name, *args, i='hi', **kwargs):
    total = 0
    print(kwargs)
    for item in kwargs.values():
        total += item
    return sum(args) + total

print(super_func('Andy', 1, 2, 3, 44, 5, num1=5, num2=10))