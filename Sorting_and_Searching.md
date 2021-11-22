# CSES - Sorting and Searching
___
## [Distinct Numbers (1621)](https://cses.fi/problemset/task/1621)
```python
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
```

## [Appartments (1084)](https://cses.fi/problemset/task/1084/)
````python
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
````

## [Ferris Wheel (1090)](https://cses.fi/problemset/task/1090/)
````python
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
````

## [Sum of Two Values (1640)](https://cses.fi/problemset/task/1640)
````python
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
````
