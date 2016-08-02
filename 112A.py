# -*- coding: utf-8 -*-

# str1 = input().upper()
# str2 = input().upper()

str1 = 'abcd'
str2 = 'sdfh'

i = 0

if str1 == str2:
	print(0)
else:
	for x in str1:
		if ord(str1[i]) > ord(str2[i]):
			print(1)
			break
		elif ord(str1[i]) < ord(str2[i]):
			print(-1)
			break
		i += 1