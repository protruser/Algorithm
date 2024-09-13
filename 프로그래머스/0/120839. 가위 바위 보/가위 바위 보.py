def solution(rsp):
    # 가위 2
    # 바위 0
    # 보  5
    answer = ''
    dic = {}
    dic['2'] = '0'
    dic['5'] = '2'
    dic['0'] = '5'
    
    for i in rsp:
        answer += dic[i]
        
    return answer