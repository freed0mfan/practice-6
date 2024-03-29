hole = input('Размеры отверстия в дм (AxB): ')
brick = input('Размеры кирпича в дм (CxDxE): ')
A = float(hole.split('x')[0])
B = float(hole.split('x')[1])
C = float(brick.split('x')[0])
D = float(brick.split('x')[1])
E = float(brick.split('x')[2])

hole_lst = [A, B]
brick_lst = [C, D, E]

if min(brick_lst) <= min(hole_lst):
    brick_lst.remove(min(brick_lst))
    if min(brick_lst) <= max(hole_lst):
        print('да')
    else:
        print('нет')
else:
    print('нет')
