
def removeLetter(st, pos): # функция удаляющая любую из букв в строках
    st = list(st)
    
    if pos == -1:
        st.pop()
    else:
        st.pop(pos)
        
    st = ''.join(st)

    return st

def removeComma(word):  # функция для проверки наличия запятой и ее исключения
    
    if (len(word) > 0 and word[len(word)-1] == ','):
                word = removeLetter(word, -1)

    return word


def findMinWord(st):
    st = st.split(' ')
    i = 0
    
    minwl = len(st[0])    #наименьшая длина слова
    
    minwp = 0             #номер наименьшего по длине слова в предложении
    
    for word in st:
        
        if len(word) < minwl:
            minwl = len(word)
            minwp = i

        i += 1

    return minwl, minwp

def findMaxWord(st):
    st = st.split(' ')
    i = 0
    
    minwl = len(st[0])    #наибольшая длина слова
    
    minwp = 0             #номер наибольшего по длине слова в предложении
    
    for word in st:
        #print(word)

        word = removeComma(word)
        
        if len(word) > minwl:
            minwl = len(word)
            minwp = i

        i += 1

    return minwl, minwp
            

def textProgram(text):

    text = ''.join(text)

    numOfMinSt = 0
    numOfMaxSt = 0

    minwl = 256
    minwp = 0

    maxwl = 0
    maxwp = 0
    
    text = text.split('.');
    text.pop()
    #print(len(text))

    i = 0
    
    for st in text:
        if st[0] == " ":
            st = removeLetter(st, 0)
            
        #print(st)
            
        res = findMinWord(st)
        
        if res[0] < minwl:
            numOfMinSt = i
            minwl = res[0]
            minwp = res[1]
            
        res = findMaxWord(st)

        if res[0] > maxwl:
            numOfMaxSt = i
            maxwl = res[0]
            maxwp = res[1]

        i += 1

    minSt = text[numOfMinSt]
    maxSt = text[numOfMaxSt]

    if minSt[0] == ' ':
        minSt = removeLetter(minSt, 0)

    if maxSt[0] == ' ':
        maxSt = removeLetter(maxSt, 0)

    minSt2 = minSt.split(' ')
    maxSt2 = maxSt.split(' ')

    minW = minSt2[minwp]
    maxW = maxSt2[maxwp]

    minSt2[minwp], maxSt2[maxwp] = maxSt2[maxwp].upper(), minSt2[minwp].upper()

    text2 = text.copy()

    text2[numOfMinSt] = ' '.join(minSt2)
    text2[numOfMaxSt] = ' '.join(maxSt2)

    minSt2[minwp], maxSt2[maxwp] = maxSt2[maxwp], minSt2[minwp]

    text[numOfMinSt] = ' '.join(minSt2)
    text[numOfMaxSt] = ' '.join(maxSt2)

    minSt2[minwp], maxSt2[maxwp] = maxSt2[maxwp], minSt2[minwp]

    minSt2 = ' '.join(minSt2)
    maxSt2 = ' '.join(maxSt2)

    text2 = '. '.join(text2)
    text2 += '.'

    
    
    text = '. '.join(text);
    text += '.'
    
    return (minSt2, maxSt2, minW, maxW, minSt2, maxSt2, text2, text)
            


text = []

text.append("Николай Ге работал над этим полотном в конце девятнадцатого века ")
text.append("в Италии и Флоренции во время его пенсионерской поездки ")
text.append("за границу. После того как он привёз картину в Петербург")
text.append(" она экспонировалась в Академической выставке конца прошлого ")
text.append("столетия. Совет Академии художеств высоко оценил мастерство")
text.append(" художника проявленное им при написании этой картины и ")
text.append("присвоил ему звание профессора исторической живописи.")



minSt, maxSt, minW, maxW, minSt2, maxSt2, text2, text = textProgram(text)

print("Исходный текст:\n")
print(text, "\n")
print("Предложение с самым коротким словом:\n");
print(minSt, "\n");
print("Предложение с самым длинным словом:\n");
print(maxSt, "\n");
ln = "Самое короткое слово - " + minW.upper()
ln += ", самое длинное слово - " + maxW.upper()
print(ln, "\n", sep="")
print("Измененный текст с переставленными местами словами:\n");
print(text2)

