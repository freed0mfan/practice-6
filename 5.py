import math as m

move = input('Ход [__-__]: ')
letter_num = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

x0 = letter_num[move[0]]
y0 = int(move[1])
x1 = letter_num[move[3]]
y1 = int(move[4])

if m.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2) == m.sqrt(5):
    print('верно')
else:
    print('ошибка')
