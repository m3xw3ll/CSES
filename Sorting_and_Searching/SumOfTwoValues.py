a, x = map(int, input().split())
n = [int(i) for i in input().split()]
temp = {}

for i in range(int(a)):
    p = n[i]
    if x - n[i] in temp:
        print(i+1, temp[x-n[i]] +1)
        quit()
    else:
        temp[n[i]] = i

print("IMPOSSIBLE")
