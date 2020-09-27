def st(a):
    if a==343:
        s=15*t
    if a==381:
        s=18*t
    if a==473:
        s=13*t
    if a==485:
        s=11*t
    return s
a=int(input('Введите код города: '))
t=int(input('Введите длительность звонка: '))
print('Стоимость звонка будет равна: ',st(a))
    
