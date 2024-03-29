cell = input('Клетка: ')
letter = cell[0]
num = int(cell[1])
letter_num = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

if (num + letter_num[letter]) % 2 == 0:
    print('черная')
else:
    print('белая')
