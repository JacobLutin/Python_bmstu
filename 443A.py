st = input()

k = 0

for i in range(ord('a'), ord('z')+1):
    x = st.count(chr(i))
    if x:
        k += 1
        
print(k)

