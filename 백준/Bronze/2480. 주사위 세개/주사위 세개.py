dice = sorted(list(map(int, input().split())), reverse=True)

diff = len(set(dice))

if diff == 3:
    print(dice[0]*100)
elif diff == 1:
    print(10000 + dice[0]*1000)
elif diff == 2:
    for i in dice:
        if dice.count(i) == 2:
            print(1000 + i*100)
            break