L = [-8, 8, 6.0, 5, 'строка', -3.1]
sum=0
for i in range(len(L)):
    if type(L[i])==int or type(L[i])==float:
        sum+=L[i]
print(sum)