# all are in different memory locations, not contiguous

dictionary = {
    'a': 1, # key: value (pair)
    'b': 2,
    'c': [1, 2, 3],
    'x': True,
    'y': 'Hello'
}

my_list = [
    {
        'a': 1, 
        'b': 2
    },
    {
        'r': [1, 2, 3],
        'l': True
    }
]

print(my_list[1]['r'][2])

print(dictionary['b'])