x = 0
d = 10240
y = x + d

start = x
step = 1
dirn = 1
done = False
dist, itn = 0, 0; 


d_vec = [10 + 1000*i for i in range(20)]
d_vec = [10, 50, 100, 300, 500, 1000, 2000, 3000, 5000, 8000, 10000, 13000, 15000, 20000]

d_vec = [13000, 16000]

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



