import numpy as np

# Метод секущих
def intersecting_method(f, x0, x1, eps, maxiter):

        iter_x = 0      # Все Х находящиеся на промежутке [a, b) (в дальнейшем - массив)
        error_code = 0  # Код ошибки
        i = 0           # Счетчик итераций

        # Проверка левого конца [a, b)
        if f(x0) == 0:
                return [x0], 0, 0

        # Существует ли корень на [a, b)
        if f(x0) * f(x1) < 0:
                
                iter_x = [x0, x1]
        
                while abs(x1 - x0) > eps and i < maxiter:

                        # Защита от деления на ноль
                        if f(x0) - f(x1) == 0:
                                error_code = 2
                                break

                        # Формула уточнения корня
                        x2 = x1 - (x0 - x1) / (f(x0) - f(x1)) * f(x1)
                        x0 = x1
                        x1 = x2
                        
                        i += 1

                        # Добавление корня в массив всех значений X полученных на [a, b)
                        iter_x.append(x2)

                # Добавление ошибки, в случае достижения максимального числа итераций
                if i == maxiter:
                        error_code = 1

        return iter_x, i, error_code

def iteration(f, a, b, h, eps, maxiter):
        
        x0 = a      # Левый конец полуинтервала [a, b)
        x1 = a + h  # Правый конец полуинтервала [a, b)

        roots = []       # Корни
        errors = []      # Ошибки
        iterations = []  # Число итераций
        segments = []    # Сегменты (x0, x1)

        while x0 < b:

                # "Отрезаем" интревал в случае его выхождения за значение b
                if x1 > b:
                        x1 = b

                # Уточнения корня на интервале
                iter_x, iter_n, error_code = intersecting_method(f, x0, x1, eps, maxiter)

                # Добавлние всех данных о корне
                if iter_x != 0:
                        roots.append(iter_x[-1])
                        errors.append(error_code)
                        iterations.append(iter_n)
                        segments.append([x0, x1])

                if x1 == b:                  
                        break

                x0 = x1
                x1 += h

        return roots, segments, iterations, errors

'''
def newton_method(f, x0, x1, eps, maxiter):

        def fp(x):
                dx = 1e-10
                return (f(x + dx) - f(x)) / dx

        iter_x = 0
        error_code = 0
        i = 0

        if f(x0) == 0:
                return [x0], i, error_code

        if f(x1) == 0:
                return [x1], i, error_code

        if f(x1) * f(x0) < 0:

                x1 = x0 - f(x0) / fp(x0)

                print('x0 = ', x0, sep='')
                print('x1 = ', x1, sep='')
                iter_x = [x0, x1]
                while abs(x1 - x0) > eps and i < maxiter:

                        x0 = x1
                        x1 = x1 - f(x1) / fp(x1)

                        print(abs(x1-x0))

                        print('x', i+2, ' = ', x1, sep='')
                        i += 1
                        iter_x.append(x1)

                if i == maxiter:
                        error_code = 1

        return iter_x, i, error_code
'''
