#print("Введите ряд чисел через пробел:")

#pol = pol = input().split()
#pol = [ int(x) for x in pol ]

pol = [9, 7, 1, 2, 1, 6, 5, 4]

d_pol = len(pol)

maxn = 0
pol_p = 0
t = 0

for i in range(1, d_pol):

    maxk = 0
    
    if i < d_pol // 2:
        t += 1
    else:
        t += -1

    k = i

    b = True

    for i in range(i+1, i+t+1):
        k -= 1
        print(pol[i], end = "")
        if (pol[i] != pol[k]):
            b = False
            #break
        maxk += 1

    print()
    
    if maxk > maxn:
        maxn = maxk
        pol_p = i

    


print()
print(pol_p, maxn)
