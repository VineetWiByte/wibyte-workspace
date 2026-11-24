import random
N = 100

L = random.sample(range(1, N+1), 5)
L = random.choices(range(1, N+1), k=110)

# Finding first duplicate (NAIVE, nested loop)
found = False
for kk in range(len(L)):
    for jj in range(kk+1, len(L), 1): 
        if L[kk] == L[jj]:
            found = True
            break
    if found: 
        break

print(L)
print(kk, jj, L[kk])


seen = set()
for kk in range(len(L)):
    if L[kk] in seen:
        break
