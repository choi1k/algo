from collections import deque
n = int(input())
card = [i+1 for i in range(n)]

card = deque(card)

while True:
    if len(card) == 1:
        print(card[0])
        break
    card.popleft()
    if len(card) == 1:
        print(card[0])
        break
    card.append(card.popleft())

    