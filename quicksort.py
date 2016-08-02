from random import *
def qSort(L):
     
    if L:
        Num = randint(0, len(L)-1)
        return qSort([x for x in L if x < L[Num]]) \
               + [x for x in L if x==L[Num]] \
               + qSort([x for x in L if x > L[Num]])
    return[]
a=[1, 0, 0, 5, -4, -5, -5, 0, 3, 5]
print(a)
a = qSort(a)
print(a)
    
