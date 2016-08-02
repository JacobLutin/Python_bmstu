st = input()

i = 0

while i < len(st):
    podst = ''
    if st[i:i+3] == 'WUB':
        i += 3
    else:
        while st[i:i+3] != 'WUB' and i < len(st):
            podst += st[i]
            i += 1
        print(podst, end=' ')
    
