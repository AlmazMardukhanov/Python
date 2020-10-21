def Maxsum(s):
    if k==-1:
        sum=0
        for i in range (len(s)):
            sum1=0
            s2=s[i+1:]+s[:i+1]
            for j in range(len(s2)):
                ans2=s2[0]
                sum1+=s2[j]
                ans2=max(ans2,sum1)
                sum1=max(sum1,0)
            sum=max(sum,sum1)

    else:
        sum=0
        s1 = s[k + 1:] + s[:k]
        ans1=s1[0]
        print(s1)
        for o in range(len(s1)):
            sum+=s1[o]
            ans1=max(ans1,sum)
            sum=max(sum,0)

    return sum


x=(int(input('Введите кол-во игр: ')))
for  i in range(x) :
    s=[]
    n,k=map(int,input('Введите кол-во секторов и номер черного сектора(если его нет введите -1): ').split())
    s = list(map(int, input('Введите значения секторов: ').split()[:n]))
    print('Максимальный результат=',Maxsum(s))