N = 100
is_prime = [True]*(N+1)
is_prime[0] = False
is_prime[1] = False

p = 2

while p*p <= N: 
    if is_prime[p]:
        for jj in range(p*p, N+1, p):
            is_prime[jj] = False
    p += 1

print(is_prime)

res = [x for x, prime in enumerate(is_prime) if prime]

print(len(res), res)

#result = []
#for x, prime in enumerate(is_prime):
#    if prime: 
#        result.append(x)
