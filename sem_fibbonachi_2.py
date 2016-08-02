n = int(input())

a = [0]*2
a[0] = 0
a[1] = 1

for i in range(2, n):
    a.append(a[i-1] + a[i-2])
print(a)

