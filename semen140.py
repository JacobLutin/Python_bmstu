for N in range(1, 10000):
    #if N<2:print('Нельзя')
    i=2;G=N
    while i<=N and N>1:
        if i==G:break
        if N%i:i+=1
        else:N//=i
print('!')
