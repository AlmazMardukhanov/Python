N=int(input('Сколько в списке будет элементов:  '))
L=list();
for i in range(0,N,1):
    x=int(input('Введите элемент: '))
    L.append(x)
print(L)
for i in range(N//2):
    t=L[i]
    L[i]=L[N//2+i]
    L[N//2+i]=t
print(L)