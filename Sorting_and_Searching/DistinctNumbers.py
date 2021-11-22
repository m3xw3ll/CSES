num = int(input())
numbers = [int(i) for i in input().split()]
numbers.sort()
count = 0
tmp = 0
for n in numbers:
    if tmp == n:
        None
    else:
        count += 1
        tmp = n

print(count)