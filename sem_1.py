a = int(input())
b = int(input())
c = int(input())

max = (a >= b) * a + (b > a) * b
max = (c >= max) * c + (max > c) * max

min = (a <= b) * a + (b < a) * b
min = (c <= min) * c + (min < c) * min

mid = a+b+c - min - max

print(min, mid, max)

print(0 or 5)
