n, k = map(int, input().split())
coin = sorted([int(input()) for _ in range(n)], reverse=True)

answer = 0
for c in coin:
    answer += k // c
    k %= c

print(answer)