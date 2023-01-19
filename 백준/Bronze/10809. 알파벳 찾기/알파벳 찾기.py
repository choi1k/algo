s = input()
alpha = "abcdefghijklmnopqrstuvwxyz"

answer = []

for a in alpha:
    if a in s:
        answer.append(s.index(a))
    else:
        answer.append(-1)

print(*answer)