n = int(input())
for _ in range(n):
    s = list(map(str, input().split()))
    for i in range(len(s)):
        s[i] = s[i][::-1]
    print(*s)