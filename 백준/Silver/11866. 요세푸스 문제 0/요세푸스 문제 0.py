from collections import deque

n, k = map(int, input().split())

num = deque([i+1 for i in range(n)])
answer = []

while num:
    for i in range(k-1):
        num.append(num.popleft())
    answer.append(num.popleft())

print("<", end="")
print(*answer, sep=", ", end="")
print(">")