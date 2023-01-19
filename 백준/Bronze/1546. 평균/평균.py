n = int(input())
num = list(map(int, input().split()))
maxnum = max(num)

for i in range(n):
    num[i] = num[i] / maxnum * 100
print(sum(num)/n)
