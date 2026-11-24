import random
import time

Nmax = 10
N = 11; 
L = random.choices(range(1, Nmax+1), k=N)
L = [3, 5, 1, 5, 3, 2]
print(L)

# Finding first duplicate (NAIVE, nested loop)
found = False
for kk in range(N):
    for jj in range(kk+1, N, 1): 
        if L[kk] == L[jj]:
            found = True
            break
    if found: 
        break

print('First item with duplicate at index', kk, L[kk])

input()

# print(kk, jj, L[kk])

#t0 = time.time()
seen = set()
for kk in range(N):
    if L[kk] in seen:
        break
    else: 
        seen.add(L[kk])


print('First item with duplicate at index', kk, L[kk])


input()
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

print(freqmap)
print('First item with duplicate at index', kk, L[kk])
