import sys
input = sys.stdin.readline

s = input().rstrip()
scnt = len(s)
q = int(input())

lst = [list(0 for i in range(26))]

for i in range(scnt):
    v = lst[i].copy()
    v[ord(s[i])-97] += 1
    lst.append(v)

for i in range(q):
    a,l,r = input().split()
    print(lst[int(r)+1][ord(a)-97]-lst[int(l)][ord(a)-97])