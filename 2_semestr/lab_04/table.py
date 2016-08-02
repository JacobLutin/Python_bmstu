
def CreateTable(results, iterations):

    width = 8

    n = 6

    line = '-' * 90


    def FormCenter(value):
        s = '{:^' + str(width) + '}'
        return s.format(value)

    def StrCenter(s):
        return str.center(s, width)

    print()

    print('  Тест  |       Упорядоченный       |         Случайный         |    Обратно упорядоченный')


    print(line)

    for i in range(iterations):
        s = FormCenter(i+1)
        print(s, end='', sep='')
        k = 0
        for result in results[i]:

            if k % 3 == 0:
                print('|', end='', sep='')
            s = FormCenter(round(result))
            print(s, end=' ', sep='')

            k += 1

        print()

    print(line)
    print()


