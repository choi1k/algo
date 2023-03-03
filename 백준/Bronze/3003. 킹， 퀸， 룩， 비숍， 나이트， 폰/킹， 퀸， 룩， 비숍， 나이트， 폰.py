chess = [1, 1, 2, 2, 2, 8]
have = list(map(int, input().split()))
answer = []
for i in range(len(chess)):
    answer.append(chess[i] - have[i])
print(*answer)