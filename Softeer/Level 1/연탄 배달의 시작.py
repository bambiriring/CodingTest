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

# https://softeer.ai/practice/7626

import sys

n = int(input())

loc = list(map(int, input().split()))

dis = []
for i in range(1, n):
    dis.append(loc[i] - loc[i-1])

min_dis = min(dis)
print(dis.count(min_dis))
