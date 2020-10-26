x=list(input('Введите число: '))
sum=0
for i in range(len(x)):
    x[i]=int(x[i])
    if x[i]%2==1:
        sum+=x[i]**2
print(sum)

