s = input()
cnt = 1
res = []
while True:
    for i in range(len(s)):
        if i+cnt <= len(s):
            res.append(s[0+i:cnt+i])
        else:
            break
    cnt+=1
    if cnt>len(s):
        break
print(len(set(res)))