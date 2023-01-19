s = input()
s = s.lower()
dic = dict()

for i in s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

maxnum = max(dic.values())
if list(dic.values()).count(maxnum) > 1:
    print("?")
else:
    key = list(dic.keys())
    val = list(dic.values())
    print(key[val.index(maxnum)].upper())