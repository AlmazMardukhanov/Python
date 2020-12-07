mas=[i for i in range(100)]
del mas[6]
for k in range(len(mas)-1):
    if mas[k+1]-mas[k]>1:
        print(mas[k+1]-1)
