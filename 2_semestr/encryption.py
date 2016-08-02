import random

m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
n = 3


class Shifr:

    def __init__(self, text, n):
        self.n = n
        decode(text)
        #self.matrix = matrix
        #self.n = len(matrix[0])

    def createEncryption(self):
        n = self.n
        encryption = []
        for i in range(n):
            encryption.append([])
            for j in range(n):
                encryption[i].append(0)
        self.encryption = encryption

    def createTable(self):
        table = []
        n = self.n
        for i in range(n):
            table.append([])
            for j in range(n):
                table[i].append(0)

        c = 1
        for i in range(n // 2):
            for j in range(n // 2):
                table[i][j] = c
                table[j][n-i-1] = c
                table[n-i-1][n-j-1] = c
                table[n-j-1][i] = c
                c = c + 1
        c = c - 1

        self.table = table

        return c, table

    def rotate(self):
        m = self.matrix
        n = self.n
        for i in range(0, n//2):
            for j in range(i, n-1-i):
                t = m[i][j]
                m[i][j] = m[n-j-1][i]
                m[n-j-1][i] = m[n-i-1][n-j-1]
                m[n-i-1][n-j-1] = m[j][n-i-1]
                m[j][n-i-1] = t
        self.matrix = m
        return m

    def decode(self, mask, out, text):
        for i in range(n):
            for j in range(n):
                if (mask[i][j] == 1):
                    encryption[i][j] = text[k]
                    k += 1
        self encryption

    def randomTable(self):
        block = []
        table = self.table

        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        flag = True
        for k in range(len(block)):
            if (table[i][j] == -1) or (table[i][j] == block[k]):
                flag = False
                break
        if (flag == True):
            block.append(table[i][j])
            table[i][j] = -1

        for i in range(n):
            for j in range(n):
                if (table[i][j] != -1):
                    table[i][j] = 0
                else:
                    table[i][j] = 1

        self.table = table

        return table, block




text = "серегаяобьяснютебекакэтоработает"
n = 8

shifr = Shifr(text, n)
shifr.createTable()
print(shifr.randomTable())
