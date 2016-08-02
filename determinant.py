# -*- coding: utf-8 -*-

import random

num = 100

a = [[0 for x in range(num)] for x in range(num)]

for i in range(num):
	for j in range(num):
		# a[i][j] = random.randint(100, 999)
		a[i][j] = random.randint(1, 9)



for i in range(num):
	print a[i]

# print a[1]