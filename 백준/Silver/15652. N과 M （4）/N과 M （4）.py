import sys
n, m = map(int, input().split())
c = [False] * (n+1)
a = [0] * n

def go(index, start, n, m):
    if index == m:
        for i in range(m):
            print(a[i], end=" ")
        print()
        return
    for i in range(start, n+1):
        # if c[i]:
        #     continue
        c[i] = True
        a[index] = i   
        go(index+1, i, n, m)
        c[i] = False

go(0, 1, n, m)