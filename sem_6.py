a = input().split()
a = [int(x) for x in a]
R = int(input())

i = 0

while i < len(a) and R > a[i]:
    i += 1

a = a[:i] + [R] + a[i:]

print(a)
