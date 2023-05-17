n = int(input())

prime = [False,False]+[True]*(n-1)
prime_list = []

for i in range(2,n+1):
    if prime[i]:
        prime_list.append(i)
        for j in range(2*i,n+1,i):
            prime[j] = False

prime_list += [0]

start,end = 0,0
prime_sum = prime_list[0]
ans = 0

while start <= end and end < len(prime_list)-1:
    if prime_sum == n:
        ans+=1
        end+=1
        prime_sum += prime_list[end]
    elif prime_sum < n:
        end+=1
        prime_sum += prime_list[end]
    elif prime_sum > n:
        prime_sum-=prime_list[start]
        start+=1
print(ans)