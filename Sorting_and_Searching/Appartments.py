n, m, k = map(int, input().split())
x = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

x.sort()
b.sort()

i = 0 #index for appartments
j = 0 #index for applicants
cnt = 0

while i < m and j < n:
    if (abs(b[i] - x[j]) <= k):
        i += 1
        j += 1
        cnt += 1
    else:
        if b[i] > (x[j] + k):
            j += 1
        else:
            i += 1

print(cnt)






