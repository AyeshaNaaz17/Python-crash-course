user = {
    'basket': [1, 2, 3],
    'greet': 'hello'
}

print(user.get('age', 55)) # if value not there, it creates that key-value pair

user2 = dict(name='Jonathan')
print(user2)