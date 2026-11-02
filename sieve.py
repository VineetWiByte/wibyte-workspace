N = 32000

import math

def is_prime(N): 
    for k in range(2, int(math.sqrt(N))+1): 
        if N % k == 0: 
            return False
    return True

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

#print(base_primes, len(base_primes))

N = 32000

base_primes = eratosthenes_sieve(N)
#new_primes = []
R = 1000000000
L = 950000000

# numbers = [x for x in range(L, R+1, 1)]
sgt_size = R - L + 1; 
primes = [True]*(sgt_size)

print(len(base_primes))
print(sgt_size)

input()
for p in base_primes:
 
  # Create the sieve
  if p*p <= R:
    start_num = L + (p - L%p)%p      
    start_idx = start_num - L
    
    n_multiples = (R - start_num)//p + 1
    
    print(start_idx, n_multiples)

    
    marks = [False]*n_multiples
    primes[start_idx: : p] = marks
    #input()
      
sgt_primes = [jj+L for jj, is_prime in enumerate(primes) if is_prime]


#for b in base_primes: 
#    if not is_prime(b): 
#        print(b)

#for s in sgt_primes: 
#    if not is_prime(s): 
#        print(s)




'''
for sgt_num in range(1, total_sgts+1): 
    numbers = [x for x in range(sgt_num*sgt_size+1,(sgt_num+1)*sgt_size+1, 1)]
    primes = [True]*sgt_size
    for p in base_primes:
        if p*p <= numbers[-1]:
            tgt = numbers[0] + (p - numbers[0]%p)%p
            idx = numbers.index(tgt)

            for jj in range(idx, sgt_size, p):
                primes[jj] = False

    sgt_primes = [numbers[jj] for jj, is_prime in enumerate(primes) if is_prime]
    print(sgt_primes)
    input()

'''































#M = 938

#for k in range(2, M//2+1, 1):
#    if is_prime[k] and is_prime[M-k]:
#        print('found', k, M-k)



#times_hit = [0]*(N+1)


#hit_by = {}
#for k in range(N+1):
#    hit_by[k] = []











'''

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
''' 