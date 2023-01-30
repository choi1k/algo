import sys
from itertools import combinations 

input = sys.stdin.readline

arr = [int(input()) for _ in range(9)]
seven = list(combinations(arr, 7))

for i in seven:
    if sum(i) == 100:
        print(*sorted(list(i)), sep="\n")
        break