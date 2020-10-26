s=list('2 aaa 3 ssss 5 ffff'.split(' '))
k=0
sum=0
max=0
for i in range(len(s)):
    if s[i].isdigit():
        s[i]=int(s[i])
        k+=1
        sum+=s[i]
        if s[i]>max:
            max=s[i]

print('Кол-во цифр=',k,'Их сумма=',sum,'Максимальное число=',max)

