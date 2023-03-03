n = int(input())
cycle = 0
new = n

while True:
    cycle += 1
    new = new%10*10 + sum(list(map(int, list(str(new)))))%10

    if new == n:
        print(cycle)
        break