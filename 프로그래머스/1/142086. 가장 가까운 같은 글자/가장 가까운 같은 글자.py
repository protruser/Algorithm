def solution(s):
    answer = []
    dic = {}
    for i in range(len(s)):
        try:
            answer.append(i - dic[s[i]])
            dic[s[i]] = i
        except:
            dic[s[i]] = i
            answer.append(-1)
            
    return answer