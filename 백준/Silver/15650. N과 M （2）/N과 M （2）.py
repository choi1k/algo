n, m = map(int, input().split())
c = [False] * (n+1)
a = [0] * m

def calc(idx, n, m):
    if idx == m:
        if a == sorted(a):
            print(*a)
        return
    for i in range(1, n+1):
        if c[i]:
            continue
        c[i] = True
        a[idx] = i
        calc(idx + 1, n, m)
        c[i] = False

calc(0, n, m)