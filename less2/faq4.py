def find_pairs(L,summ):
    s = set(L)
    edgeCase = summ/2
    if L.count(edgeCase) ==2:
        print (edgeCase, edgeCase)
    s.remove(edgeCase)      
    for i in s:
        diff = summ-i
        if diff in s: 
            print (i, diff)

L = [2,45,7,3,5,1,8,9]
summ = 10          
find_pairs(L,summ)
