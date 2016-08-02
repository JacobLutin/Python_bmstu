from math import exp

b = float(input())
if b >= 0:
    const = 1 - b**(1/2)
else:
    print('Cant do it')
x = 0.5

i = 0
while x < 3:
    i += 1

    z = (1/(x*x))*exp(-x)*const
    
    x += 0.1

print(z, i)

zrange = int((3 - 0.5)/0.1)

print(zrange)

for i in range(5, 30):
    x = i / 10
    print(x)
