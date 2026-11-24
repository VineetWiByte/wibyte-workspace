import random
import time

Nmax = 100
N = 10000; 
#L = random.choices(range(1, Nmax+1), k=N)
L = list(range(1, N+1))

#L = [3, 5, 1, 5, 3, 2]
# Finding first duplicate (NAIVE, nested loop)
t0 = time.perf_counter()
found = False
for kk in range(N):
    for jj in range(kk+1, N, 1): 
        if L[kk] == L[jj]:
            found = True
            break
    if found: 
        break
elapsed_L = time.perf_counter() - t0

print(elapsed_L* 10**6)
#print(kk, jj, L[kk])

#t0 = time.time()
#seen = set()
#for kk in range(N):
#    if L[kk] in seen:
#        break
#    else: 
#        seen.add(L[kk])

#t1 = time.time()
#print(t1-t0)


t0 = time.perf_counter()
freqmap = {}
# Pass 1
for nums in L:
    if freqmap.get(nums, 0) == 0: 
        freqmap[nums] = 1
    else: 
        freqmap[nums] += 1

# Pass 2
for kk in range(len(L)):
    if freqmap[L[kk]] > 1: 
        found = True
    break

#print(kk)

elapsed_D = time.perf_counter() - t0; 
print(elapsed_D*10**6)
