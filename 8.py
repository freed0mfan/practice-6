import random

vanya = [0]
for _ in range(201):
    vanya.append(random.randint(1, 201))

n = int(input('порядковый номер числа из ряда: '))
print(f'Число: {vanya[n - 1]}')
