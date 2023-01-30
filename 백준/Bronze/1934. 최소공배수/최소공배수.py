import math

def lcm(a, b):
    return a * b // math.gcd(a,b)

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    print(lcm(a,b))