# Farmer initial
x = 0
d = 100
y = x + d
dist = 0
# y is cow

start = x
step = 1
dirn = 1
itn = 0

done = False

while not done: 
    itn += 1
    stop = x + dirn*step

    #print(start, stop)

    if (dirn == 1 and start <= y <= stop)or(dirn == 1 and stop <= y <= start): 
        dist += abs(start - y)
        done = True
        
    else:
        dist += abs(start - stop) 
        start = stop
        step *= 2
        dirn *= -1

print('***')
print(d, itn, dist)