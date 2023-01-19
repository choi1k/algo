hour, minute = map(int, input().split())

total = hour * 60 + minute
total -= 45

if total < 0:
    total = 60 * 24 + total

hour = total // 60
minute = total % 60

print(hour, minute)
