t = int(input())

for i in range(t):
    a, b = [int(i) for i in input().split()]
    if b > a:
        a, b = b, a
        if a > 2 * b or ((a + b) % 3 != 0):
            print("NO")
        else:
            print("YES")
    else:
        if a > 2 * b or ((a + b) % 3 != 0):
            print("NO")
        else:
            print("YES")