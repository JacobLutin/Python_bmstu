def new_increment(a):
    i = int(len(a) / 2)
    yield i
    while i != 1:
        if i == 2:
            i = 1
        else:
            i = int(numpy.round(i/2.2))
        yield i


arr = [1, 2, 3, 4]

print(new_increment(arr))