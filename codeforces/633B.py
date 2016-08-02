#m = int(input())
#m = 1




def fact(x):

    result = 1

    for i in range(2, x+1):
        result *= i

    print(result)



def program(m):

    print(m)

    x = 1
    result = []

    m = 10**m
    
    for i in range(1, 10000):

        x *= i

        if x % m == 0 and x % (m*10) != 0:
            result.append(i)

    print(len(result))

    for i in result:
        print(i, end=' ')
    print()

for i in range(1, 31):
    program(i)
