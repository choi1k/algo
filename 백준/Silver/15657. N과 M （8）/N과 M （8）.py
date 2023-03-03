import sys
n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))

c = [False] * (n+1)
a = [0] * m

def go(index, start, n, m):
    if index == m:
        print(*a)
        return
    for i in range(start, n):
        # if c[i]:
        #     continue
        c[i] = True
        a[index] = num[i]
        go(index+1, i, n, m)
        c[i] = False

go(0, 0, n, m)