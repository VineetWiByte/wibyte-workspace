import random
import time

Nmax = 100
N = 110; 
L = random.choices(range(1, Nmax+1), k=N)

# Finding first duplicate (NAIVE, nested loop)

found = False
for kk in range(N):
    for jj in range(kk+1, N, 1): 
        if L[kk] == L[jj]:
            found = True
            break
    if found: 
        break

print(L)
print(kk, jj, L[kk])


seen = set()
for kk in range(N):
    if L[kk] in seen:
        break
    else: 
        seen.add(L[kk])

print(kk, L[kk])
