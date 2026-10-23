Nrows = 5

print('Basic Rectangle Pattern')
print()
for kk in range(Nrows):
    print('*'*Nrows)


input()
print('Last aligned Triangle')
for kk in range(Nrows):
    print('*'*(kk+1))

input()


# Left aligned Inverted triangle
print('Left Aligned Inverted Triangle')
for kk in range(Nrows):
    print('*'*(Nrows-kk))

# Right aligned triangle
print()
input()

print('Right Aligned Triangle')
for kk in range(Nrows):
    print(' '*(Nrows-kk-1) + '*'*(kk+1))

input()
print('Right Aligned Inverted Triangle')
for kk in range(Nrows):
    print(' '*kk + '*'*(Nrows-kk))


input()
print('Left Aligned triangle')
for kk in range(Nrows):
    if kk <= 2: 
        print('*'*(kk+1))
    else: 
        print('*'*(Nrows- kk))


input()
print('Right Aligned triangle')
for kk in range(Nrows):
    if kk <= 2: 
        print(' '*(2 - kk) + '*'*(kk+1))
    else: 
        print(' '*(kk-2) + '*'*(Nrows- kk))


input()
print('1-2-3 Diamond')
for kk in range(Nrows):
    if kk <= 2: 
        print(' '*(2 - kk) + '* '*(kk+1))
    else: 
        print(' '*(kk-2) + '* '*(Nrows- kk))


input()
print('1-3-5 Diamond')
for kk in range(Nrows):
    if kk <= 2: 
        print(' '*(2 - kk) + '*'*(2*kk+1))
    else: 
        print(' '*(kk-2) + '*'*(9- 2*kk))



input()
print('Hollow 1-3-5 Diamond')
for kk in range(Nrows):
    if kk <= 2: 
        print(' '*(2 - kk) + '*'*(2*kk+1))
    else: 
        print(' '*(kk-2) + '*'*(9- 2*kk))







# Filled Parallelogram
print('Left Aligned Parallelogram')
input()

for kk in range(Nrows):
    print(' '*(kk) + '*'*5)
    

# Filled Parallelogram (Right Aligned)
print()
input()

for kk in range(Nrows):
    print(' '*(Nrows-kk-1) + '*'*5)


# Hollow Rectangle (Right Aligned)
print('Hollow Rectangle')
input()


for kk in range(Nrows):
    if kk == 0 or kk == 4:
        print('*'*5)
    else:
        print('*' + ' ' * 3 + '*')


# Hollow Rectangle (Right Aligned)
print('Hollow Parallelogram')
input()


for kk in range(Nrows):
    if kk == 0 or kk == 4:
        print(' ' * kk + '*'*5)
    else:
        print(' ' * kk + '*' + ' '*3 + '*')








# Right aligned inverted triangle
print()
input()

for kk in range(Nrows):
    print(' '*(kk) + '*'*(Nrows-kk))



input()
print('Hollow 1-2-3 Diamond')
for kk in range(Nrows):
    if kk <= 1: 
        print(' '*(2 - kk) + '* '*(kk+1))
    elif kk == 2: 
        print(' '*(2 - kk) + '* ' + ' '*2 + '*')
    else: 
        print(' '*(kk-2) + '* '*(Nrows- kk))

print('Square with a nested loop')

Ncols = 5

for kk in range(Nrows):
    for jj in range(Ncols): 
        print('*', end = '')
    print()



print('Parallelogram with a nested loop')

Ncols = 5

for kk in range(Nrows):
    for jj in range(kk): 
        print(' ', end = '')
    for jj in range(5):
        print('*', end = '')
    print()

input()
print('1-3-5 Diamond with a nested loop')
Ncols = 5
for kk in range(Nrows):
    for jj in range(Ncols): 
        if kk <= 2: 
            if jj < 2 - kk or jj > 2 + kk: 
                print(' ', end = '')
            else: 
                #print(kk, jj)
                print('*', end = '')
        else: 
            if jj < kk - 1 or jj > 7 - kk: 
                print(' ', end = '')
            else: 
                print('*', end = '')
    print()        



input()
print('1-3-5 Diamond with a nested loop (scanning)')
Ncols = 5

for kk in range(Nrows):
    if kk <= 2: 
        for jj in range(2-kk): 
            print(' ', end = '')
        for jj in range(2*kk+1): 
            print('*', end = '')
    else: 
        for jj in range(kk-2): 
            print(' ', end = '')
        for jj in range(9 - 2*kk): 
            print('*', end = '')
    print()


input()
print('Hollow 1-3-5 Diamond with a nested loop (x/y coordinate)')

Ncols = 5

for kk in range(Nrows):
    for jj in range(Ncols): 
        if kk ==  jj or kk == 4-jj: 
            print('*', end = '')
        else: 
            print(' ', end = '')
    print()
    



