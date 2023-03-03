n = int(input())
cnt = 1
num = 1

while True:
    if n <= num:
        print(cnt)
        break
    num += 6 * cnt
    cnt += 1
    