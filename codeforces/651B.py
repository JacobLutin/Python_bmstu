
n = int(input())
A = input().split()
A = [int(x) for x in A]
A.sort()

X = []

while len(A) > 0:

    B = []

    for item in A:

        if item not in B:
            B.append(item)
            
            A[A.index(item)] = 0
    
    A = [x for x in A if x > 0]
    
    for i in B:
        X.append(i)

k = 0
for i in range(len(X)-1):
    if X[i] < X[i+1]:
        k += 1
    
print(k)
