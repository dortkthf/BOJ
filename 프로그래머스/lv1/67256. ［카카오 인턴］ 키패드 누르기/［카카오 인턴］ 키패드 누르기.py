def solution(numbers, hand):
    answer = ''
    phone = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    dic = {}

    
    for i in range(4):
        for j in range(3):
            dic[phone[i][j]] = (i,j)
            
    l_current = dic['*']
    r_current = dic['#']
    
    for i in numbers:
        if i in (1,4,7):
            answer+='L'
            l_current = dic[i]
        elif i in (3,6,9):
            answer+='R'
            r_current = dic[i]
        else:
            if abs(dic[i][0]-l_current[0])+abs(dic[i][1]-l_current[1]) == abs(dic[i][0]-r_current[0])+abs(dic[i][1]-r_current[1]):
                if hand == 'left':
                    answer+='L'
                    l_current = dic[i]
                else:
                    answer+='R'
                    r_current = dic[i]
            else:
                if abs(dic[i][0]-l_current[0])+abs(dic[i][1]-l_current[1]) > abs(dic[i][0]-r_current[0])+abs(dic[i][1]-r_current[1]):
                    answer+='R'
                    r_current = dic[i]
                else:
                    answer+='L'
                    l_current = dic[i]
    return answer
