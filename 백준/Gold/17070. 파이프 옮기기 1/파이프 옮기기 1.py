n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

def go(x, y, dir):
    if x == n-1 and y == n-1:
        return 1
    answer = 0
    
    if dir == 0:
        if y+1 < n and a[x][y+1] == 0:
            answer += go(x, y+1, 0)
        if x + 1 < n and y + 1 < n and a[x][y+1] == 0 and a[x+1 ][y] == 0 and a[x+1][y+1] == 0:
            answer += go(x+1, y+1, 1)
    elif dir == 1:
        if y+1 < n and a[x][y+1] == 0:
            answer += go(x, y+1, 0)
        if x+1 < n and a[x+1][y] == 0:
            answer += go(x+1, y, 2)
        if x + 1 < n and y + 1 < n and a[x][y+1] == 0 and a[x+1 ][y] == 0 and a[x+1][y+1] == 0:
            answer += go(x+1, y+1, 1)
    elif dir == 2:
        if x+1 < n and a[x+1][y] == 0:
            answer += go(x+1, y, 2)
        if x + 1 < n and y + 1 < n and a[x][y+1] == 0 and a[x+1 ][y] == 0 and a[x+1][y+1] == 0:
            answer += go(x+1, y+1, 1)

    return answer

print(go(0,1,0))