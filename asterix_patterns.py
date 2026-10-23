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
    print(' '*(Nrows-kk) + '*'*(kk+1))



# Filled Parallelogram
print()
input()

for kk in range(Nrows):
    print(' '*(kk) + '*'*5)
    

# Filled Parallelogram (Right Aligned)
print()
input()

for kk in range(Nrows):
    print(' '*(Nrows-kk-1) + '*'*5)


# Hollow Rectangle (Right Aligned)
print()
input()

for kk in range(Nrows):
    if kk == 0 or kk == 4:
        print('*'*5)
    else:
        print('*' + ' ' * 3 + '*')








# Right aligned inverted triangle
print()
input()

for kk in range(Nrows):
    print(' '*(kk) + '*'*(Nrows-kk))


# Square with Gaps
for kk in range(Nrows):
    print('* '*Nrows)


