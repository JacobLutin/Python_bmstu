st = "gcdaz abcd aAa Abcde tt tvg".split()
st = input("Введите строку, состоящую из слов: ").split()
maxlen = 0
minlen = 255

for word in st:
    b = True
    for i in range(ord('A'), ord('Z')+1):
        k = word.count(chr(i)) + word.count(chr(i+32))
        if k > 1:
            b = False
            break
    if b and len(word) > maxlen:
        maxlen = len(word)
        maxword = word
    if b and len(word) < minlen:
        minlen = len(word)
        minword = word

if maxlen:
    print("Самое короткое слово - ", minword)
    print("Самое длинное слово  - ", maxword)
else:
    print("Таких слов в строке нет")
    
