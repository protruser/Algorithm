def solution(picture, k):
    answer = []
    for pixel in picture:
        string = ''
        for i in pixel:
            if i == '.':
                string += '.'*k
            else:
                string += 'x'*k
        
        for j in range(k):
            answer.append(string)
        
    return answer