n,m = map(int,input().split())
pokemon = { i:input() for i in range(n)}
pokemon2 = { v:k for k,v in pokemon.items()}

res = []
for i in range(m):
    str = input()
    if str.isdigit() == True:
        res.append(pokemon[int(str)-1])
    else:
        res.append(pokemon2[str]+1)
print(*res, sep='\n')