A = [4, 3, 2, 1]
v = 10

p = None

for i in range(1, len(A)):
	if A[i] == v:
		p = i
	key = A[i]
	j = i - 1
	while j >= 0 and A[j] > key:
		A[j + 1] = A[j]
		j -= 1
	A[j + 1] = key

print(A)
print(p)