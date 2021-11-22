# Introductory Problems

## [Weird Algorithm (1068)](https://cses.fi/problemset/task/1068/)
````python
n = int(input())
while n > 1:
    print(n, end=" ")
    n = n * 3 + 1 if n % 2 else n // 2
print(1)
````

## [Missing Number (1083)](https://cses.fi/problemset/task/1083)
````python
n = int(input())
print(n * (n + 1) // 2 - sum(map(int, input().split())))

````

## [Repetitions (1069)](https://cses.fi/problemset/task/1069)
````python
dna = list(str(input()))
max = 0
cnt = 0
 
for i in range(len(dna)-1):
    if dna[i] == dna[i+1]:
        cnt += 1
        if cnt >= max:
            max = cnt
    elif dna[i] != dna[i+1]:
        cnt = 0
 
print(max+1)
````

## [Increasing Array (1094)](https://cses.fi/problemset/task/1094)
```python
n = input()
x = list(map(int, input().split()))
prev = x[0]
cnt = 0
 
for i in x:
    if i < prev:
        cnt += prev - i
    else:
        prev = i
 
print(cnt)
```

## [Bit Strings (1617)](https://cses.fi/problemset/task/1617)
````python
n = int(input())
print(2**n % (10**9+7))

````

## [Palindrome Reorder (1755)](https://cses.fi/problemset/task/1755)
````python
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


````