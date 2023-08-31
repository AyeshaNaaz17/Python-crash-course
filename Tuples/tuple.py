# cannot be changed once created
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[2])
print(5 in my_tuple)

# tuple in a dictionary
user = {
    (1, 2): [1, 2, 3],
    'greet': 'Hello',
    'age': 20
}
print(user[(1, 2)])

new_tuple = my_tuple[1:2]
x = my_tuple[2]
print(x)
print(new_tuple) # only single element so (2, )

x, y, z, *other = (1, 2, 3, 4, 5)
print(x)
print(y)
print(z)
print(other)

# tuple methods
print(my_tuple.count(5))
print(my_tuple.index(3))
print(len(my_tuple))