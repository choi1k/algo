n, m = map(int, input().split())
card = list(map(int, input().split()))

answer = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            total = card[i] + card[j] + card[k]
            if total > m:
                continue
            if answer < total <= m:
                answer = total

print(answer)