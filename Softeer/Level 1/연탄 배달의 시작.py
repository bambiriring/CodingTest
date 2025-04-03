# https://softeer.ai/practice/7626

import sys

n = int(input())

loc = list(map(int, input().split()))

min_dt = 1000000
cnt= 0
for i in range(0, n):
    for j in range(i+1, n):
        if loc[j]-loc[i]< min_dt:
            min_dt = loc[j]-loc[i]
            cnt = 1
        elif loc[j]-loc[i]==min_dt:
            cnt +=1
print(cnt)
