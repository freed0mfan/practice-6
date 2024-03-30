import turtle as t

lt_up_x1 = int(input('x верхней левой вершины первого прямоугольника: '))
lt_up_y1 = int(input('y верхней левой вершины первого прямоугольника: '))
rt_btm_x1 = int(input('x нижней правой вершины первого прямоугольника: '))
rt_btm_y1 = int(input('y нижней правой вершины первого прямоугольника: '))
lt_up_x2 = int(input('x верхней левой вершины второго прямоугольника: '))
lt_up_y2 = int(input('y верхней левой вершины второго прямоугольника: '))
rt_btm_x2 = int(input('x нижней правой вершины второго прямоугольника: '))
rt_btm_y2 = int(input('y нижней правой вершины второго прямоугольника: '))

center_x1 = (lt_up_x1 + rt_btm_x1) / 2
center_y1 = (lt_up_y1 + rt_btm_y1) / 2
center_x2 = (lt_up_x2 + rt_btm_x2) / 2
center_y2 = (lt_up_y2 + rt_btm_y2) / 2


def recktangle(lt_up_x, lt_up_y, rt_btm_x, rt_btm_y):
    t.teleport(lt_up_x, lt_up_y)
    for i in range(2):
        t.fd(rt_btm_x - lt_up_x)
        t.rt(90)
        t.fd(lt_up_y - rt_btm_y)
        t.rt(90)


recktangle(lt_up_x1, lt_up_y1, rt_btm_x1, rt_btm_y1)
recktangle(lt_up_x2, lt_up_y2, rt_btm_x2, rt_btm_y2)


def check_relative_position(rect1, rect2):
    x1_rect1, y1_rect1, x2_rect1, y2_rect1 = rect1
    x1_rect2, y1_rect2, x2_rect2, y2_rect2 = rect2

    if x2_rect1 < x1_rect2 or x2_rect2 < x1_rect1 or y2_rect1 < y1_rect2 or y2_rect2 < y1_rect1:
        return "Прямоугольники лежат вне друг друга, не касаясь"
    elif (x1_rect1 >= x1_rect2 and x2_rect1 <= x2_rect2) and (y1_rect1 >= y1_rect2 and y2_rect1 <= y2_rect2):
        return "Один прямоугольник лежит внутри другого, не касаясь"
    elif (x1_rect2 >= x1_rect1 and x2_rect2 <= x2_rect1) and (y1_rect2 >= y1_rect1 and y2_rect2 <= y2_rect1):
        return "Один прямоугольник лежит внутри другого, не касаясь"
    elif (x1_rect1 < x2_rect2 and x2_rect1 > x1_rect2) and (y1_rect1 < y2_rect2 and y2_rect1 > y1_rect2):
        return "Прямоугольники имеют пересечение"
    else:
        return "Прямоугольники имеют касание"


rect1 = (lt_up_x1, lt_up_y1, rt_btm_x1, rt_btm_y1)
rect2 = (lt_up_x2, lt_up_y2, rt_btm_x2, rt_btm_y2)

print(check_relative_position(rect1, rect2))
t.done()
