s = list('a aa dfdfdfaaa aaaa'.split())
index = 0
max=0
for i in range(len(s)):
    if len(s[i]) > max:
        index=i
        max = len(s[i])
print('Номер первого самого длинного слова: ',index+1)