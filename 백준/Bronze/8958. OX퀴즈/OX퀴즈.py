n = int(input())

for _ in range(n):
    result = input()
    
    cnt = 0
    answer = 0
    for r in result:
        if r == "O":
            answer += 1 + cnt
            cnt += 1
        else:
            cnt = 0
    print(answer)