print("Введите ряд чисел:")

pol = input().split()
pol = [int(x) for x in pol]

md_pol = (len(pol) // 2) + (len(pol) % 2)
k = md_pol - (len(pol) % 2)

b = True

for i in range(md_pol, len(pol)):
    k -= 1
    if (pol[i] != pol[k]):
        b = False
        break

if b:
    print("YES")
else:
    print("NO")
