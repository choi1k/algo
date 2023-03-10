import sys
n, m = map(int, input().split())
c = [False] * (n+1)
a = [0] * m

def go(index, start, n, m):
    if index == m:
        print(*a)
        return
    for i in range(start, n+1):
        if c[i]:
            continue
        c[i] = True
        a[index] = i   
        go(index+1, i+1, n, m)
        c[i] = False

go(0, 1, n, m)