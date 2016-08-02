
a, b = input().split()
a = int(a)
b = int(b)

m = 0

while a > 0 and b > 0:

    if a > b:
        a -= 2
        b += 1
    else:
        a += 1
        b -= 2

    if a < 0 or b < 0:
        break

    m += 1

print(m)
