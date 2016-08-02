N = 4
A = [1, 1, 0, 0]
B = [1, 1, 1, 1]

A = A.reverse
B = B.reverse

C = [0]

for i in range(N):
	
	s = A[i] + B[i] + C[i]
	print(A[i], B[i], C[i])

	if s > 1:
		C.append(0)
		C[i+1] += 1
	else:
		C[i] = s

# print(C)