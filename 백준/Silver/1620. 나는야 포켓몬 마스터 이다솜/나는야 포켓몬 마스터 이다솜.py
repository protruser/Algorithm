import sys
N,M = map(int, input().split())

dic = {}
for i in range(N):
    A = sys.stdin.readline().rstrip()
    dic[A] = i+1

r_dic =dict(map(reversed, dic.items()))
for i in range(M):
    quiz = sys.stdin.readline().rstrip()
    if 65 <= ord(quiz[0]) <= 122:
        print(dic[quiz])
    else:
        print(r_dic[int(quiz)])