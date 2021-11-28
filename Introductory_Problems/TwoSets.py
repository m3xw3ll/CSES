n = int(input())
l1 = []
l2 = []
s = (n * (n+1)) / 2
target = s / 2

if s % 2 != 0:
    print("NO")
else:
    print("YES")
    for i in range(n,0,-1):
        if i <= target:
            l1.append(i)
            target -= i
        else:
            l2.append(i)

    print(len(l1))
    print(*l1)
    print(len(l2))
    print(*l2)