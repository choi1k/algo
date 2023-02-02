def check(password):
    conso = 0
    vowel = 0

    for i in password:
        if i in 'aeiou':
            vowel += 1
        else:
            conso += 1
    return conso >= 2 and vowel >= 1

def go(n, alpha, password, i):
    if len(password) == n:
        if check(password):
            print(password)
        return
    if i == len(alpha):
        return
    go(n, alpha, password + alpha[i], i+1)
    go(n, alpha, password, i+1)



l, c = map(int, input().split())
alpha = list(map(str, input().split()))
alpha.sort()
go(l, alpha, "", 0)