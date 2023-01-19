num = list(input().split())
num[0] = num[0][::-1]
num[1] = num[1][::-1]

print(max(num))