#2.1
def Tf(TC):
    TF=9/5*TC+32
    return TF
TC=int(input('Введите температуру в цельсиях: '))
TF=Tf(TC)
print('Температура в фаренгейтах=',TF)
