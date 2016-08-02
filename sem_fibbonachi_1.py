n = int(input())

a0 = 0
a1 = 1

for i in range(n-1):
    a0, a1= a1, a0 + a1

print(a1)
