from proc1 import *
from proc2 import *
from proc3 import *
from proc4 import *
from proc5 import *
def main():
    print('Выберите процедуру:')
    print('1)Отметить на графике корни.')
    print('2)Отметить на графике точки экстремума.')
    print('3)Отметить на графике точки перегиба.(В разработке)')
    print('4)Вывести точки по выбору.')
    print('5)Площади между графиками.')
    print()
    t = int(input('Введите номер процедуры: '))
    print()
    if t == 1:
        main1_graf()
    elif t == 2:
        main2_extrem()
    elif t == 3:
        main3_peregib()
    elif t == 4:
        flags = []
        print('1,0 - включить модуль или нет')
        print('1)Точки корней.')
        print('2)Точки экструмумов.')
        print('3)Точки перегибов.')
        flags = list(map(int,input('Введите какие точки отображать: ').split()))
        print()
        print()
        main4_all_proc(flags[0],flags[1],flags[2])
    elif t == 5:
        main5_peresech()
main()
