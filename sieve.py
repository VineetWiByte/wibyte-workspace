N = 100

def eratosthenes_sieve(N): 
    # Return ALL primes from 0 to N. 
    is_prime = [True]*(N+1)
    is_prime[0] = False
    is_prime[1] = False

    p = 2
    

    while p*p <= N: 
        if is_prime[p]:
            for jj in range(p*p, N+1, p):
                is_prime[jj] = False
            
        p += 1

    res = [x for x, prime in enumerate(is_prime) if prime]
    return res

base_primes = eratosthenes_sieve(32000)
print(base_primes, len(base_primes))



















#M = 938

#for k in range(2, M//2+1, 1):
#    if is_prime[k] and is_prime[M-k]:
#        print('found', k, M-k)



#times_hit = [0]*(N+1)


#hit_by = {}
#for k in range(N+1):
#    hit_by[k] = []













input()

twin_cnt = 0

for k in range(2, N-1, 1):
    if is_prime[k] and is_prime[k+2]:
        print('twin found', k, k+2)
        twin_cnt += 1

print()
print(twin_cnt)


input()



#print(times_hit)


#print(hit_by)


#print(len(res), res)

#result = []
#for x, prime in enumerate(is_prime):
#    if prime: 
#        result.append(x)
#times_hit = [0]*(N+1)
#hit_by = {}
#for k in range(N+1):
#    hit_by[k] = []
#           times_hit[jj]+=1
#            hit_by[jj].append(p)
 