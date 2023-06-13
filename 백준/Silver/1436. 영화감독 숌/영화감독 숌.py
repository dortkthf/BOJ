cnt = 0
n = int(input())
for i in range(666*10000000):
    if '666' in str(i):
        cnt+=1
        if cnt==n:
            print(i)
            break