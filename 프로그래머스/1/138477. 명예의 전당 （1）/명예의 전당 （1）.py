def solution(k, score):
    answer = []
    result = []
    for i in score:
        answer.append(i)
        answer.sort()
        if len(answer) <= k:
            result.append(answer[0])
        else:
            del answer[0]
            result.append(answer[0])
    
    return result