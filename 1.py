import math as m

size = input('Размер в формате AxB [м^2]: ')
A = float(size.split('x')[0])
B = float(size.split('x')[1])
d = m.sqrt(A ** 2 + B ** 2)

if d <= 13:
    print('да')
else:
    print('нет')
