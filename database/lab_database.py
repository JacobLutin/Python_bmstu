from math import *

_ln = '-' * 82
_f = '{:^10}|'


def getRow(row):

    row = row.split()

    for i in range(2, len(row)):

        row[i] = float(row[i])

    return row

def setAverage(row):
    if len(row) == 6:
        k = 0
        average = 0
        for i in range(3, len(row)):
            average += row[i]
            k += 1
        average = average / 3
        row.append(average)
    return row


def databaseConnect(name):

    name += '.txt'
    f = open(name, 'r', encoding='utf8')

    global database
    global databaseTitle

    i = 0

    for row in f:
        if i == 0:
            databaseTitle = row.split()
        elif len(row) > 0:
            row = getRow(row)
            row = setAverage(row)
            database.append(row)
        i += 1

    #database.pop()


def databaseSave():

    global database

    name = db + '.txt'
    f = open(name, 'w', encoding='utf8')

    titles = ' '.join(databaseTitle)
    titles += '\n'
    f.write(titles)
    for record in database:
        record = ' '.join(map(str, record))
        record += '\n'
        f.write(record)


def databaseCreate():

    global database

    database = []

    databaseSave()

def printRecords(records = ''):

    print(_ln)
    title = '|'

    for record in databaseTitle:
        title += record.center(10, ' ') + '|'
    print(title)

    if records == '':
        for record in database:

            row = '|'
            row += record[0].center(12, ' ') + '|'
            row += record[1].center(12, ' ') + '|'

            for i in range(2, len(record)):

                if trunc(record[i]) == record[i]:
                    row += _f.format(int(record[i]))
                else:
                    row += _f.format('{:.1f}'.format(record[i]))

            print(_ln)
            print(row)

    else:
        for j in records:
            record = database[j].copy()

            row = '|'
            row += record[0].center(12, ' ') + '|'
            row += record[1].center(12, ' ') + '|'


            for i in range(2, len(record)):

                if trunc(record[i]) == record[i]:
                    row += _f.format(int(record[i]))
                else:
                    row += _f.format('{:.1f}'.format(record[i]))



            print(_ln)
            print(row)

    print(_ln)


def addRecord():

    global database
    title = databaseTitle.copy()
    title.pop()
    record = []
    i = 0
    for row in title:
        st = "Введите поле \"" + row + "\": "
        inp = input(st)
        if i > 1:
            record.append(float(inp))
        else:
            record.append(inp)
        i += 1

    record = setAverage(record)
    print()
    database.append(record)

    databaseSave()

    print("Запись успешно добавлена")

def searchGet(remove = False):

    if remove:
        print("  Выберите поле, по которому запись будет удалена")
    else:
        print("  Выберите поле для поиска")

    i = 1
    for field in databaseTitle:
        line = "   " + str(i) + " - " + field
        print(line)
        i += 1

    print("   0", "- Назад")
    inp = input(" > ")

    i = 0
    search = []
    global searchFrom

    if inp != "0":
        num = int(inp) - 1
        if remove:
            print("  Записи с каиими значениями должны быть удалены?")
        else:
            print("  Введите значение для поиска")
        inp = input(" > ")

        for record in searchFrom:
            try:
                inp = float(inp)
            except:
                inp = inp

            if record[num] == inp:
                search.append(i)

            i += 1
    SearchFrom = search.copy()
    return(SearchFrom)

def searchRecord(remove = False):

    global searchFrom
    searchFrom = database.copy()

    search = []

    result = searchGet(remove)

    while True:
        print("Добавить еще поле? (да\нет)")
        inp = input(" > ")
        if inp == "нет":
            break
        elif inp == "да":
            result = searchGet(remove)


    if result == []:
        print("Таких записей не существует")
        return []

    printRecords(result)
    return result

def removeField():

    global database

    toRemove = searchRecord(True)

    if toRemove == []:
        return

    remove = []

    for i in toRemove:
        remove.append(database[i])

    for record in remove:
        database.remove(record)

    databaseSave()

    print("Найденные записи успешно удалены")



def exitProgram():
    print()

def databaseMenu():

    inp = ''

    while inp != '0':

        print(_ln)
        print("  Меню")
        print("   1 - Создать новую базу данных")
        print("   2 - Вывести записи")
        print("   3 - Добавить запись")
        print("   4 - Поиск по полю")
        print("   5 - Удаление по полю")
        print("   0 - Выход")
        inp = input(" > ")
        print(_ln)
        command(inp)()


def command(x):
    x = int(x)
    return [exitProgram, databaseCreate, printRecords,
            addRecord, searchRecord, removeField, ][x]

db = 'db'
databaseTitle = ''
searchFrom = []
database = []
databaseConnect(db)
databaseMenu()
