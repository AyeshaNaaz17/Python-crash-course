user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

print('age' in user.keys())
print('hello' in user.values())

print(user.items())

user2 = user.copy()
print(user2)

print(user.pop('age'))
print(user.popitem()) # removes any item

print(user)
print(user.update({'ages': [20, 21, 22]}))
print(user)

print(user.clear()) # clears the dictionary

print(user)
print(user2)