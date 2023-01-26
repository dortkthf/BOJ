Used1 = [0] * 40
Used2 = [0] * 40
Used3 = [0] * 40

cnt = 0
N = int(input())

def func(x):
    global cnt
    if x == N:
        cnt += 1
        return
    for i in range(N):
        if Used1[i] or Used2[i+x] or Used3[x-i+N-1]:
            continue
        Used1[i] = 1
        Used2[i+x] = 1
        Used3[x-i+N-1] = 1
        func(x+1)
        Used1[i] = 0
        Used2[i + x] = 0
        Used3[x - i + N - 1] = 0

func(0)
print(cnt)