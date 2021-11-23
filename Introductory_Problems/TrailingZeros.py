# mathematical background: https://www.purplemath.com/modules/factzero.htm
n = int(input())
fact = 1
cnt = 0

while (n // 5**fact) != 0:
    cnt += n // 5**fact
    fact += 1

print(cnt)