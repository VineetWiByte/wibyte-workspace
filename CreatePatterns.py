Nrows = 15
Ncols = 15
mid = int((Nrows- 1)/2)

for k in range(Nrows):
    for j in range(Ncols):
        if j == k or j == (Nrows - k - 1): 
            print('*', end='')
        else: 
            print(' ', end='')
    print()





input()

for k in range(Nrows):
    if k <= mid: 
        for j in range(mid-k):
            print(' ', end = '')
        for j in range(2*k+1): 
            print('*', end='')
    else: 
        for j in range(k-mid):
            print(' ', end = '')
        for j in range(2*Nrows-1-2*k): 
            print('*', end='')

    print()


    #if k <= mid: 
    #    print(' '*(mid-k) + '*'*(2*k+1))
    #else:  
    #    print(' '*(k-mid) + '*'*(2*Nrows -2*k-1))



input()

for k in range(Nrows):

    if k <= mid: 
        if k == 0: 
            print(' '*(mid-k) + '*')
        else: 
            print(' '*(mid-k) + '*' + ' '*(2*k-1) + '*')
    else: 
        if k == Nrows - 1: 
            print(' '*(k-mid) + '*')
        else: 
            print(' '*(k-mid) + '*' + ' '*(2*Nrows -2*k-3) + '*')



    





    #if k <= mid: 
    #    if k == 0: 
    #        print(' '*(mid-k) + '*')
    #    else: 
    #        print(' '*(mid-k) + '*' + ' '*(2*k-1) + '*')
    #else: 
    #    if k == Nrows - 1: 
    #        print(' '*(k-mid) + '*')
    #    else: 
    #        print(' '*(k-mid) + '*' + ' '*(2*Nrows -2*k-3) + '*')

    
    #if k == 0 or k == Nrows - 1: 
    #    print(' '* k + '*'*Ncols)
    #else: 
    #    print(' '* k + '*' + ' '*(Ncols - 2) + '*')
    
    
    
    
    
    