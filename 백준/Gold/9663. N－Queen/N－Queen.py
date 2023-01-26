import sys
input = sys.stdin.readline

n = int(input())

row = [0 for i in range(n)]
find = []
ans = 0

def n_queens(x):
    global ans, find
    if x == n:
        ans+=1
        return
    for i in range(n):
        if i in find:
            continue
        if x>=1:
            if abs(row[x-1]-i) == 1:
                continue
        row[x] = i
        for j in range(x):
            if row[j] == row[x] or abs(row[x]-row[j]) == abs(x-j):
                break
        else:
            find.append(i)
            n_queens(x+1)
            find.remove(i)

n_queens(0)
print(ans)