for item in 'All is Well':
    print(item)

for item in [1, 2, 3, 4, 5]:
    print(item)

for item in (1, 2, 3, 4, 5):
    print(item)
    
for item in {1, 2, 3, 4, 5}:
    print(item)
print(item)

for item in (1, 2, 3, 4, 5):
    for x in ['a, 'b'', 'c', 'd']:
        print(item, x)

# iterable - list, dictionary, tuple, set, string
# iterate - one by one check each item in the collection

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user.items():
    print(item)

for item in user.keys():
    print(item)

for item in user.values():
    print(item)
    
for k, v in user.items():
    print(k ,v)