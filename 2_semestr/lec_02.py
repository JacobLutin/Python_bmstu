import numpy as np

# Специальные функции формирования векторов

# Функция range работает с целыми числами
# Описаниe
# arrange([start, ] stop, [step, ] dtype=None)
# start - начало интервала
# stop - конец интервала
# step - шаг

a = np.arange(10)
print(a)

b = np.arange(2, 10)
print(b)

c = np.arange(10, 2, -2)
print(c, '\n\n')


# Функция linspace
# Описание
# linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None_
# start - начало интервала
# stop - конец интервала
# num - число элеметнов
# endpoint - если

a = np.linspace(0, 2, 5)
print(a)

b = np.linspace(0, 2, 5, endpoint = False)
print(b)

c = np.linspace(0, 5)
print(c)
