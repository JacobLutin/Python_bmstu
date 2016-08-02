# -*- coding: utf-8 -*-

num = 30

matrix = [[" " for x in range(num)] for x in range(num)]




# y = f(x)
# f(x) = x**2
# y = x**2

x = 0;
y = 0;

while y < num:
	y = x*4-5
	if y >= num: break
	matrix[y][x] = "*"
	x += 1


for i in range(num-1, -1, -1):
	for j in range(num):
		print matrix[i][j],
	print
