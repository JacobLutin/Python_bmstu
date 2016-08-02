s = raw_input()

word = "hello"

k = 0

for i in range(len(s)):
	if s[i] == word[k]:
		print(word[k])
		k += 1


if k == 5:
	print("YES")
else:
	print("NO")

