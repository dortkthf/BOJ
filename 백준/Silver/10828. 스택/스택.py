import sys
input = sys.stdin.readline

n = int(input())

stacks = []

for _ in range(n):
    a = input().rstrip()
    if a[:4] == 'push':
        k,v = a.split(' ')
        stacks.append(int(v))
    elif a == 'top':
        if len(stacks) != 0:
            print(stacks[-1])
        else:
            print(-1)
    elif a == 'size':
        print(len(stacks))
    elif a == 'empty':
        if len(stacks) != 0:
            print(0)
        else:
            print(1)
    elif a == 'pop':
        if len(stacks) != 0:
            print(stacks.pop())
        else:
            print(-1)