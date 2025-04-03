# https://softeer.ai/practice/7695

import sys

min_y = 1001
min_x = 0

n = int(input())
for i in range(n):
    x,y = map(int, input().split())
    if y < min_y:
        min_y = y
        min_x = x

print(min_x,min_y)
