n = int(input())

S = []

R = [ ]

for i in range(n):
    S.append(input())

for i in range(n-1, -1, -1):

    if S[i] not in R:
        R.append(S[i])
        print(S[i])
