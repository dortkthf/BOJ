import math

r = int(input())
ans = round(math.pi*(r**2),6)
ans2 = round((r**2)*2,6)
print(format(ans, '.6f'))
print(format(ans2, '.6f'))