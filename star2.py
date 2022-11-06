#increment
for i in range(0,5):
    for j in range(0,i+1):
        print('*',end=" ")
    print()
print('----------------------------')

#decrement
for i in range(5):
    for j in range(i,5):
        print('*',end=' ')
    print()
print('----------------------------')

#both increment and drecrement
for i in range(0,5):
    for j in range(0,i):
        print('*',end=" ")
    print()
for i in range(5):
    for j in range(i,5):
        print('*',end=' ')
    print()
print('---------------------------')

for i in range(5):
    for j in range(i,5):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    print()
for i in range(5):
    for j in range(i):
        print(' ',end=' ')
    for j in range(i,5):
        print('*',end=' ')
    print()
print('---------------------------')

for i in range(5):
    for j in range(0,i):
        print('*',end=" ")
    print()
for i in range(5):
    for j in range(i,5):
        print('*',end=' ')
    print()
print('----------------------------')


for i in range(5):
    for j in range(i,5):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
print('----------------------')


for i in range(5):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,5):
        print('*',end=' ')
    print()
print('----------------------')






