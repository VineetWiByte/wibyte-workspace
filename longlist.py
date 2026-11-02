import time


#data = list(range(10_000_000))
data = list(range(5000000))
N = 3

# Modify every 3rd item in-place

t0 = time.time()
for i in range(0, len(data), N):
    data[i] = -1


target_len = len(range(0, len(data), N))

# Replace every 3rd item in-place
data[::N] = [-1] * target_len

t1 = time.time()
print(t1 - t0)