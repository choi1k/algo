n, x = map(int, input().split())
arr = list(map(int, input().split()))
rtn = []
for i in arr:
    if i < x:
        rtn.append(i)

print(*rtn)