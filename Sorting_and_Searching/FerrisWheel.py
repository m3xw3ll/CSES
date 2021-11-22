n, x = map(int, input().split())
p = [int(i) for i in input().split()]
cnt = 0

p.sort()

light = 0 #index for lightest child
heavy = n-1 #index for heaviest child

while light <= heavy:
    if p[light] + p[heavy] > x:
        cnt += 1
        heavy -= 1
    else:
        cnt += 1
        light += 1
        heavy -= 1

print(cnt)