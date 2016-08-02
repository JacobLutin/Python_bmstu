from math import sqrt

X = input().split()
X = [int(x) for x in X]

sum = 0

for x in X:
    sum += x**2

X = [print("{:.2f}".format(x/sqrt(sum)) for x in X]
    
