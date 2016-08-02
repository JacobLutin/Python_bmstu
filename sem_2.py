x = float(input(""))
eps = float(input())

y = 1
a = 1

i = 0

while abs(a) >= eps:
    i += 2
    a *= -((x * x)/((i-1) * i))
    y += a

print(y)


    
    
