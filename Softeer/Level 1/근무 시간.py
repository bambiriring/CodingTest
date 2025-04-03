import sys

t = 0
for i in range(5):
    a, b = input().split()
    # print(a, b)
    t = t + int(b[0:2])*60+int(b[3:5])-int(a[0:2])*60-int(a[3:5])
    # print(t)
print(t)   
