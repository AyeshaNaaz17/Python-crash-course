i = 1
while i < 20:
    print(i)
    i += 1;

while i < 20:
    print(i)
    break

print('-----')

my_list = [1, 2, 3]
j = 0
while j < len(my_list):
    print(my_list[j])
    j += 1

while True:
    input('say something: ')
    break

while True:
    response = input('say something: ')
    if response == 'bye':
        break