a=[1,2,3,4,2,3,6]
S=set()
M=[]
for i in a:
    if i not in S:
        S.add(i)
        M.append(i)
print(M)
