x = 0
d = 10
y = x + d

start = x
step = 1
dirn = 1
done = False
dist, itn = 0, 0; 


while not done:
    stop = x + dirn*step
    itn += 1
    print(start, stop)

    if (dirn == 1 and start <= y <= stop) or (dirn == -1 and stop <= y <= start):
        # Target Found
        dist += abs(y - start)
        done = True
    else:
        # Account for the steps
        dist += abs(start - stop)
        # Reverse the direction and continue
        start = stop
        step *= 2
        dirn *= -1
        
print(itn, dist)



