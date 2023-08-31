basket = ['a', 'b', 'c', 'd', 'e', 'a']

# print(basket.sort()) # gives none

basket.sort()
print(basket)

print(sorted(basket))
print(basket)

new_basket = basket[:]
# or new_basket = basket.copy()
print(new_basket)
print(basket)

# to reverse
basket.reverse()
print(basket)