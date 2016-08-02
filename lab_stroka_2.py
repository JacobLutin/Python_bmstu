from math import *

st1 = input("Первое число: ")
st2 = input("Второе число: ")

st1 = [int(i) for i in st1]
st2 = [int(i) for i in st2]

#for i in range

if max(st1) > max(st2):
    rmax = max(st1)
else:
    rmax = max(st2)

if len(st1) > len(st2):
    rlen = len(st1)
    for i in range(rlen-len(st2)):
        st2.insert(0, 0)
else:
    rlen = len(st2)
    for i in range(rlen-len(st1)):
        st1.insert(0, 0)
    
result = [0] * (rlen)

ost = 0

for i in range(rlen-1, -1, -1):
    
    r = st1[i] + st2[i] + ost
    if r > rmax:
        result[i] = r - rmax - 1
        ost = 1
    else:
        result[i] = r
        ost = 0
    #print(st1[i], '+', st2[i], '=', result[i], 'остаток =', ost)

if ost:
    result.insert(0, ost)

print("Результат:   ", end='')

for x in result:
    print(x, sep='', end='')

