x = 0
d = 10240
y = x + d

start = x
step = 1
dirn = 1
done = False
dist, itn = 0, 0; 


d_vec = [10*2**i for i in range(12)]

for d in d_vec: 
    y = x + d
    done = False
    dist, itn, step, start = 0, 0, 1, x
    while not done:
        stop = x + dirn*step
        itn += 1
        

        if (dirn == 1 and start <= y <= stop) or (dirn == -1 and stop <= y <= start):
            # Target Found
            dist += abs(y - start)
            done = True
        else:
            # Account for the steps
            dist += abs(start - stop)
            # Reverse the direction and continue
            start = stop
            step += 1
            dirn *= -1
        
    print(d, itn, dist)



