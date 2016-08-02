"""
Сформировать новый массив из положительных элементов старого
"""

a = input()
b = [int(x) for x in a if int(x)>0]
print(b)

#62

a = list(map(int, input().split()))
b = [x for x in a if x>0]
print(b)

#68

