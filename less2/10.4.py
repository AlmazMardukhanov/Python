import random
print('Угадайте число')
x=random.randint(1,10)
y=0
while y!=x:
    y=input('Введите число или "Выход": ')
    if y=='Выход':
        break
    else:
        y=int(y)
        if y>x:
            print('Ваше число больше')
        elif y<x:
            print('Ваше число меньше')

print('Вы угадали!')


