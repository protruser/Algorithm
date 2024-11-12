def solution(s):
    lst = []
    
    for i in s:
        if i == "(":
            lst.append(i)
        
        if i == ')':
            if len(lst) == 0:
                return False
            
            if lst[-1] == '(':
                lst.pop()
            else:
                return False
    
    if len(lst) == 0:
        return True
    else:
        return False
        
    return True