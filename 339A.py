
s = input()

a = []

a = s.split('+')

s = ''

for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

s += a[0]
a[0] = -1

for x in a:
    if x != -1:
        s += '+'
        s += x

print(s)
