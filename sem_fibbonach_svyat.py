n = int(input())

F = [0, 1]

F = [ F.append(F[i-2] + F[i-1]) for i in range(2, n) ]

print(F)
