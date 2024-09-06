def solution(order):
    # 차가운 것 4500
    # 뜨거운 것 5000
    # 아무거나 -> 차가운 아메리카노
    answer = 0
    
    for i in order:
        if "americano" in i:
            answer += 4500
        
        elif "cafelatte" in i:
            answer += 5000
            
        else:
            answer += 4500
            
    return answer