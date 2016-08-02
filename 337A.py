n, m = input().split()
n = int(n)
m = int(m)
f = input().split()
f = [int(i) for i in f]

if n == m:
    print(max(f)-min(f))
else:
    minr = 1000
    for i in range(m):
        j = 0
        k = 0
        fr = []
        while k < n:
            if j != i:
                fr.append(f[j])
                k += 1
            j += 1
        print(fr)
        if (max(fr) - min(fr)) < minr:
            minr = max(fr) - min(fr)

    print(minr)


    
