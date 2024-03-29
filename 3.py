cordon = input('NxM: ')
N = int(cordon.split('x')[0])
M = int(cordon.split('x')[1])
K = int(input('K: '))

i = 1
j = 1
result1 = 0
result2 = 0
while i in range(1, N):
    if i * M == K:
        result1 = 1
        break
    else:
        i += 1
while j in range(1, M):
    if j * N == K:
        result2 = 1
        break
    else:
        j += 1

if result1 == 1 or result2 == 1:
    print('успешно')
else:
    print('неосуществимо')
