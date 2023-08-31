basket = ['a', 'b', 'c', 'd', 'e']
print(len(basket))

# adding - append method
new_basket = basket.append('f')
print(basket)
print(new_basket) # gives none because append function does not return anything to store in the new basket list

# to make basket list store in the new basket
new_basket = basket
print(new_basket)

# insert method
basket.insert(5, 'g')
print(basket)

# extend method
new_basket = basket.extend(['h', 'i'])
print(basket)
print(new_basket) # gives none because extend function does not return


# removing
basket.pop() # removes last item
print(basket)
basket.pop(0) # removes the item of the index specified
new_basket = basket.pop(1)
print(new_basket) # gives the popped item as pop returns the value removed


new_basket = basket.clear() # clears everything in the list
print(basket)