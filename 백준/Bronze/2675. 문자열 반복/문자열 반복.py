t = int(input())

for _ in range(t):
    r, s = input().split()
    r = int(r)
    answer = ""
    for i in s:
        answer += i*r
    print(answer)