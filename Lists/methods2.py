basket = ['a', 'b', 'c', 'd', 'e', 'b']

print(basket.index('b'))
print(basket.index('c', 0, 3)) # starts the search from 0th index and stops before 2

# in keyword
print('a' in basket)
print('i' in 'hi my name is Ian')

print(basket.count('b'))