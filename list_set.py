import time
N = 100000
L = list(range(N))
Nruns = 100
elapsed_L, elapsed_S = 0.0, 0.0

for _ in range(Nruns):
    start = time.perf_counter()
    found = N in L
    elapsed = time.perf_counter() - start
    elapsed_L += elapsed 

    S = set(L)

    start = time.perf_counter()
    found = N in S
    elapsed= time.perf_counter() - start
    elapsed_S += elapsed

print('elapsed list =', elapsed_L/Nruns * 10**6, 'micro seconds')
print('elapsed set =', elapsed_S/Nruns * 10**6, 'micro seconds')