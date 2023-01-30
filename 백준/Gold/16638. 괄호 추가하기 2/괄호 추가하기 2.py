n = int(input())
a = list(input())
m = (n+1) // 2 - 1
answer = None

for s in range(1 << m):
    ok = True
    for i in range(m-1):
        if (s&(1<<i)) > 0 and (s&(1<<(i+1))) > 0:
            ok = False
    if not ok:
        continue
    b = a[:]
    for i in range(m):
        if (s & (1 << i)) > 0:
            k = 2*i + 1
            b[k-1] = '(' + b[k-1]
            b[k+1] = b[k+1] + ')'

    c = ''.join(b)

    temp = eval(c)

    if answer is None or answer < temp:
        answer = temp

print(answer)