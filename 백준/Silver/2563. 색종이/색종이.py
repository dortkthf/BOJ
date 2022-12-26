n = int(input())
res = [list(0 for i in range(100)) for i in range(100)]
for i in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            res[i][j] = 1
cnt = 0
for i in res:
    cnt += sum(i)
print(cnt)
