n = str(input())
chars = sorted(list(set(n)))
first = ''
middle = ''
m = 0

for i in chars:
    cnt = n.count(i)
    if cnt % 2 == 0:
        first += i * (cnt // 2)
    elif m == 1:
        first = 0
        print("NO SOLUTION")
        break
    else:
        middle = i
        m = 1
        first += i * ((cnt-1)//2)

if first != 0:
    print(first + middle + first[::-1])

