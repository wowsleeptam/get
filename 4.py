s=input()
lit = set()

dic = dict()

for i in s:
    o=ord(i)
    if ord(i) != 32:
        lit.add(i)

for i in lit:
    dic[i]=0


for j in s:
    if j in lit:
        dic[j]+=1

sorted_tuple = sorted(dic.items(), key=lambda x: x[0])
for i in sorted_tuple:
    print(*i)
