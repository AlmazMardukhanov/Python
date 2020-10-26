import random

n = 5
m = 3
x = [[random.randint(1, 10) for i in range(n)] for i in range(m)]
for i in x:
    print()
    for j in i:
        print(j, end=" ")
kol = 0
num_str = 0
for i in range(m):
    for j in range(n):
        kol_new = x[i].count(x[i][j])
        if kol_new > kol:
            kol = kol_new
            num_str = i

print()
print(num_str+1)
