import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

def count(list, left, right):
    r_index = bisect_right(list, right)
    l_index = bisect_left(list, left)
    return r_index - l_index

n = int(input())
num = sorted(list(map(int, input().split())))
m = int(input())
card = list(map(int, input().split()))

for i in card:
    print(count(num, i, i), end = ' ')