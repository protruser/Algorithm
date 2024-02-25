import sys

S,P = map(int, sys.stdin.readline().split())
pw = input()
A,C,G,T = map(int, sys.stdin.readline().split())
cnt = 0
dic = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0}

part = pw[0:P]
for i in part:
    dic[i] += 1

a,b = 0,P-1
while 1:
    if dic['A'] >= A and dic['C'] >= C and dic['G'] >= G and dic['T'] >= T:
        cnt += 1

    if b == S-1:
        break
    
    dic[pw[a]] -= 1
    a += 1
    b += 1
    dic[pw[b]] += 1

print(cnt)