import math

def solution(r1, r2):
    answer = 0
    for x in range(r2+1):
        maxy = int((r2**2-x**2)**(1/2))
        if x >= r1:
            miny = 0
        else:
            if int((r1**2-x**2)**(1/2)) < (r1**2-x**2)**(1/2):
                miny = int((r1**2-x**2)**(1/2))+1
            else:
                miny = int((r1**2-x**2)**(1/2))
        answer+=(maxy-miny+1)
    return answer*4-(r2-r1+1)*4