import itertools

m, n = map(int, input().split())
data = [i+1 for i in range(m)]

answer = list(itertools.product(data,repeat = n))

for i in answer:
    print(*i)