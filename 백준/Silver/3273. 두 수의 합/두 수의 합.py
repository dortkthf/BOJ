n = int(input())
numbers = list(map(int,input().split()))
x = int(input())

numbers.sort()

cnt = 0

start = 0
end = n-1

while start < end:
    if numbers[start]+numbers[end] == x:
        cnt+=1
        end-=1
    elif numbers[start]+numbers[end] < x:
        start+=1
    else:
        end-=1
print(cnt)