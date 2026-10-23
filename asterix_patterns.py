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
print('Diamond')
for kk in range(Nrows):
    if kk <= 2: 
        print(' '*(2 - kk) + '* '*(kk+1))
    else: 
        print(' '*(kk-2) + '* '*(Nrows- kk))




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
print('Hollow Diamond')
for kk in range(Nrows):
    if kk <= 1: 
        print(' '*(2 - kk) + '* '*(kk+1))
    elif kk == 2: 
        print(' '*(2 - kk) + '* ' + ' '*2 + '*')
    else: 
        print(' '*(kk-2) + '* '*(Nrows- kk))



