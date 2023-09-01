# scope - what variables do I have access to

x = 10
def some_function():
    total = 100
    print(x)
    
# print(total) - gives error because variable total scope is only inside function

some_function()

a = 1

def parent():
    a = 90
    def confusion():
        return a
    return confusion()

print(parent())
print(a)

# 1 - start with local variable
# 2 - Parent local variable
# 3 - Global variable
# 4 - Built-in python function


# globals

count = 0

def counting():
    global count 
    count += 1
    return count

counting()
counting()
print(counting())

def counting(count):
    count += 1
    return count



print(counting(counting(counting(count))))

print("---------------------")

# nonlocal keyword

def outer(): # 1
    x = 'local' # 2
    def inner(): # 4
        # nonlocal x
        x = 'nonlocal'
        print("inner: ", x)
    
    inner() # 3
    print("outer: ", x)

outer()

def outer2(): # 1
    x = 'local' # 2
    def inner2(): # 4
        nonlocal x
        x = 'nonlocal'
        print("inner2: ", x)
    
    inner2() # 3
    print("outer2: ", x)

outer2()