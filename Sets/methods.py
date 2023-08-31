my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

print(my_set.difference(your_set))  # {1, 2, 3}

print(my_set.discard(5)) # None
print(my_set) # {1, 2, 3, 4}

print(my_set.difference_update(your_set))
print(my_set)

print(my_set.intersection(your_set)) # {4, 5}

print(my_set.isdisjoint(your_set)) # checks if there's anything common

print(my_set.union(your_set)) # joins both sets

print(my_set | your_set) # same operation as union, for intersection it's &

print(my_set.issubset(your_set))

print(your_set.issuperset(my_set))