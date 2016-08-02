A = list(map(int,input().split()))
k = int(input())
A.append(0)
for i in range(len(A)):
    if A[i]>k:
        for j in range(len(A)-1,i-1,-1):
            A[j] = A[j-1]
        A[i] = k
        break
print(A)
