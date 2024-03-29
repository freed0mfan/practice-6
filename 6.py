N_K_M = input('N_K_M: ')
N = int(N_K_M.split(' ')[0])
K = int(N_K_M.split(' ')[1])
M = int(N_K_M.split(' ')[2])

time = N//K * 2*M

if N % K != 0:
    time += 2*M
print(time)
