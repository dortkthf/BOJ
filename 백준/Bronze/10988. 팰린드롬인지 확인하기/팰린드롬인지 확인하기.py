l = (input())
ll = len(l)
j = False
for i in range(ll//2):
    if l[i] != l[ll-1-i]:
        print(0)
        break        
else:
    print(1)