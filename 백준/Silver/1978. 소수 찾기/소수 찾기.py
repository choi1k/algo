import math

n = 1000
arr = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i] == True:
        j = 2
        while i * j <= n:
            arr[i*j] = False
            j += 1
arr[1] = False

N = int(input())
num = list(map(int, input().split()))
count = 0
for i in num:
    if arr[i] == True:
        count += 1

print(count)