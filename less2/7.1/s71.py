import math
##Вычисляет площадь треугольника по формуле Герона
def s(a,b,c):
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    return s
if __name__=='__main__':
    import doctest
    doctest.testmod()
