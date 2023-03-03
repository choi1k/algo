n = int(input())
time = sorted(list(map(int, input().split())))

print(sum([(n-i) * time[i] for i in range(n)]))