n,m = map(int, input().split())
nm = list(input() for i in range(n))

nm2 = []
for i in nm:
    nm2.append(i)
nm2.reverse()

nm3 = []
for i in nm2:
    k = list(i)
    k.reverse()
    kk = ''.join(k)
    nm3.append(kk)

nm4 = []
for i in nm:
    k = list(i)
    k.reverse()
    kk = ''.join(k)
    nm4.append(kk)

nn = n-8
mm = m-8
dp = []
res = []

for i in range(nn+1):
    for j in range(mm+1):
        dp.append([i,j])

for d in dp:
    base = nm[d[0]][d[1]]
    cnt = 0
    for i in range(d[0],d[0]+8,2):
        for j in range(d[1],d[1]+8,2):
            if nm[i][j] != base :
                cnt+=1
            if nm[i+1][j] == base :
                cnt+=1
        for j in range(d[1]+1,d[1]+8,2):
            if nm[i][j] == base: 
                cnt+=1
            if nm[i+1][j] != base:
                cnt+=1
    res.append(cnt)

for d in dp:
    base = nm3[d[0]][d[1]]
    cnt = 0
    for i in range(d[0],d[0]+8,2):
        for j in range(d[1],d[1]+8,2):
            if nm3[i][j] != base :
                cnt+=1
            if nm3[i+1][j] == base :
                cnt+=1
        for j in range(d[1]+1,d[1]+8,2):
            if nm3[i][j] == base: 
                cnt+=1
            if nm3[i+1][j] != base:
                cnt+=1
    res.append(cnt)

for d in dp:
    base = nm2[d[0]][d[1]]
    cnt = 0
    for i in range(d[0],d[0]+8,2):
        for j in range(d[1],d[1]+8,2):
            if nm2[i][j] != base :
                cnt+=1
            if nm2[i+1][j] == base :
                cnt+=1
        for j in range(d[1]+1,d[1]+8,2):
            if nm2[i][j] == base: 
                cnt+=1
            if nm2[i+1][j] != base:
                cnt+=1
    res.append(cnt)
    
for d in dp:
    base = nm4[d[0]][d[1]]
    cnt = 0
    for i in range(d[0],d[0]+8,2):
        for j in range(d[1],d[1]+8,2):
            if nm4[i][j] != base :
                cnt+=1
            if nm4[i+1][j] == base :
                cnt+=1
        for j in range(d[1]+1,d[1]+8,2):
            if nm4[i][j] == base: 
                cnt+=1
            if nm4[i+1][j] != base:
                cnt+=1
    res.append(cnt)

print(min(res))