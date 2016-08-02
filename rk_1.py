print("Введите ряд чисел через пробел:")

pol = input().split()
pol = [ int(x) for x in pol ]

d_pol = len(pol) // 2

pol1 = []
pol2 = []

for i in range(d_pol):
    pol1.append(pol[i])

if (len(pol) % 2 == 0):
    d_pol -= 1
    

for i in range(len(pol)-1, d_pol, -1):
    pol2.append(pol[i])

                
if pol1 == pol2:
    print("YES")
else:
    print("NO")
