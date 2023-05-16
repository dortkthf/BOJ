n = int(input())
numbers = list(map(int,input().split()))
x = int(input())

numbers.sort()

def two_pointer(start,end,cnt):
    while start < end:
        if numbers[start]+numbers[end] == x:
            cnt+=1
            end-=1
        elif numbers[start]+numbers[end] < x:
            start+=1
        else:
            end-=1
    return cnt

print(two_pointer(0,n-1,0))