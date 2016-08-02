n = int(input())

likes = input().split()
likes = [int(x) for x in likes]

likes.reverse()
maxlike = 0
max = 0
x = []

for i in likes:
    if i not in x:
        x.append(i)
        if likes.count(i) >= max:
            max = likes.count(i)
            maxlike = i

print(maxlike)
