st = input()

st += ' '

i = 0
k = 0

while i < len(st):
    if st[i] == 'а' or st[i] == 'А':
        k += 1        
        while st[i] == 'а' or st[i] == 'А':
            i += 1
    i += 1

if k:
    print(k)
else:
    print('NO')
