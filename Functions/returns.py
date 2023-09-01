def sum(num1, num2):
    return num1 + num2

# function - > should do something and return something
print(sum(2, 4))

total = sum(10, 5)
print(sum(10, total))

def summ(num1, num2):
    def another_sum(n1, n2):
        return n1 + n2
    return another_sum(num1, num2)
    print('Hello')
    
summ(10, 23)