from collections import deque
n, m, start = map(int, input().split())
arr = [[] for _ in range(n+1)]
check = [False] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
for i in range(1, n+1):
    arr[i].sort()

def dfs(x):
    global check
    check[x] = True
    print(x, end=' ')
    for y in arr[x]:
        if check[y] == False:
            dfs(y)

def bfs(start):
    check = [False] * (n+1)
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()
        print(x, end = ' ')
        for y in arr[x]:
            if check[y] == False:
                check[y] = True
                q.append(y)

dfs(start)
print()
bfs(start)
print()