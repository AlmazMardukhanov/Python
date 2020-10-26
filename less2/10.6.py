sum=0
while True:
    x=input('Введите число или "Стоп": ')
    if str(x)=='Стоп':
        break
    else:
        sum+=int(x)
print('Сумма чисел = ',sum)