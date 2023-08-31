# unordered collections of unique objects
# does not support indexing

my_set = {1, 2, 3, 4, 5}
print(my_set)
new_set = {1, 2, 3, 4, 5, 5}
print(new_set)

my_set.add(100)
my_set.add(2)
print(my_set)

my_list = [1, 2, 3, 4, 5, 5]
print(set(my_list))

print(2 in my_set)
set2 = my_set.copy()
my_set.clear()
print(set2)
print(my_set)