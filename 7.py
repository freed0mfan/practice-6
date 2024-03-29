K = int(input('K: '))

result = 0
for n in range(1000):
    for m in range(1000):
        if 5 * n + 7 * m == K:
            result = 1

if result == 1:
    print('да')
else:
    print('нет')
