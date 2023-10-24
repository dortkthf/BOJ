import heapq

def solution(operations):
    answer = [0,0]
    mn = []
    mx = []
    
    for op in operations:
        cmd, num = op.split(' ')
        if cmd == 'I':
            heapq.heappush(mx, -int(num))
            heapq.heappush(mn,int(num))
        else:
            if num == '1' and mx:
                mn.remove(-heapq.heappop(mx))
            elif num =='-1' and mn:
                mx.remove(-heapq.heappop(mn))
    if mx:
        answer = [-heapq.heappop(mx),heapq.heappop(mn)]
    return answer