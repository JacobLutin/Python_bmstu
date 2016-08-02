# -*- coding: utf-8 -*-

array = map(int, raw_input().split())

length = len(array) - 1

for i in range(0, length):
	for j in range(0, length):
		if array[j] > array[j+1]:
			array[j], array[j+1] = array[j+1], array[j]


print array