def highest_even(li):
    even = li[0]
    for item in li:
        if item % 2 == 0:
            even = max(even, item)
    return even       

print(highest_even([10, 2, 3, 4, 11]))