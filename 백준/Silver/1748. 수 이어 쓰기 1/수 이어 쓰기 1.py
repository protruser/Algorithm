N = int(input())
answer = 0
a='0'
b='9'
cnt = 1
while 1:
    if int(a) < N < int(b):
        answer += (N-int(a))*cnt
        break
    else:
        answer += (int(b)-int(a))*cnt
        a += '9'
        b += '9'
        cnt += 1

print(answer)