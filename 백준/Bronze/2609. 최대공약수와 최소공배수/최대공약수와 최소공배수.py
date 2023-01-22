import math

def lcd(a, b):
    return a*b // math.gcd(a, b)

a, b = map(int, input().split())

print(math.gcd(a, b))
print(lcd(a, b))