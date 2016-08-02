
a = list(map(float, input().split()))

k = 0

min = 0
max = 0

maxn = -1
minn = -1

for i in range(len(a)):
    if a[i] > 0:
        min = min or a[i]
        k += 1
        if a[i] <= min:
            min = a[i]
            minn = i
    elif a[i] < 0:
        max = max or a[i]
        if a[i] >= max:
            max = a[i]
            maxn = i
    
if maxn == -1 and minn == -1:
    print("В массиве нет ни отрицательных, ни положительных элементов.")
elif minn == -1:
    print("В массиве нет положительных элементов.")
elif minn == -1:
    print("В массиве нет отрицательных элементов.")
else:
    a[minn],a[maxn] = a[maxn],a[minn]
    
print(a) #измененный массив

print(k) #кол-во положительных элементов
