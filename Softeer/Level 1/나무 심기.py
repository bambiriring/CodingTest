# https://softeer.ai/practice/7353

import sys

n = int(input())

nums = list(map(int, input().split()))

nums.sort(reverse=True)
max_num = max(nums[0]*nums[1], nums[n-1]*nums[n-2])
print(max_num)
