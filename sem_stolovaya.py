a = input().split()
a = [int(x) for x in a]
R = int(input())

if R > a[-1:][0]:
    a += R
else:
    for i in range(len(a)):
        if a[i] > R:
            a.append(0)
            buf = a[i]
            a[i] = R
            k = i+1
            break

                   
    for i in range(k, len(a)):
        a[i], buf = buf, a[i]

print(a)
    
    

