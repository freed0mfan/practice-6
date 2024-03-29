import turtle as t
import math as m

x1 = float(input('x1: '))
y1 = float(input('y1: '))
r1 = float(input('r1: '))
x2 = float(input('x2: '))
y2 = float(input('y2: '))
r2 = float(input('r2: '))

t.teleport(x1, y1-r1)
t.circle(r1)
t.teleport(x2, y2-r2)
t.circle(r2)
t.done()

d = m.sqrt((x2-x1)**2 + (y2-y1)**2)

if d > r1:
    if d == r1+r2:
        print('Окружности имеют внешнее касание')
    elif d > r1+r2:
        print('Окружности одна вне другой, не касаются')
    else:
        print('Окружности пересекаются')
else:
    if r1 == d+r2:
        print('Окружности имеют внутренне касание')
    elif r1 > d + r2:
        print('Одна окружность лежит внутри другой, не касаясь')
    else:
        print('Окружности пересекаются')
