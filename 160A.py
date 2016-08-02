
n = int(input())

a = input().split()

a = [int(i) for i in a]

for i in range(n):
    for j in range(n-1):
        if a[j] < a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]


sl = a[0]
sr = 0

if n > 1:
    for i in range(1, n):
        sr += a[i]

k = 1

while sl <= sr:
    sl += a[k]
    sr -= a[k]
    k += 1

print(k)
