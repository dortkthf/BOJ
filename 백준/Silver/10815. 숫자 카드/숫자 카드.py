n = int(input())
list1 = set(map(int,input().split()))
m = int(input())
list2 = list(map(int,input().split()))

for i in list2:
    if i in list1:
        print(1, end=' ')
    else:
        print(0, end=' ')