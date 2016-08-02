A = [8, 7, 6, 5, 4, 3, 2, 1]
# A = input().split()

# A = [int(x) for x in A]

for j in range(2, len(A)):
	key = A[j]
	i = j - 1
	while i > 0 and A[i] > key:
		
		A[i+1] = A[i]
		i = i - 1
	A[i+1] = key
	print(A)

print(A)

for j = 2 to A.length  
    key = A[j]
    i = j - 1
    while i > 0 and A[i] > key
         A[i+1] = A[i]
         i = i - 1
    A[i+1] = key