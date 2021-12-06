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

## [Permutations (1070)](https://cses.fi/problemset/task/1070/)
````python
n = int(input())

if n == 2 or n == 3:
    print("NO SOLUTION")
else:
    for i in range(2, n + 1, 2):
        print(i, end=" ")
    for i in range(1, n + 1, 2):
        print(i, end=" ")
````

## [Number Spiral (1071)](https://cses.fi/problemset/task/1071/)
````python
t = int(input())

for i in range(t):
    y, x = map(int, input().split())

    if x > y:
        if x % 2 == 1:
            print(x * x -y +1)
        else:
            x -= 1
            print(x * x +y)
    else:
        if y % 2 == 0:
            print(y * y -x +1)
        else:
            y -= 1
            print(y * y + x)
````

## [Two Knights (1072)](https://cses.fi/problemset/task/1072/)
````python
n = int(input())

for i in range(1,n+1,1):
    possible_steps = (i**4 - i**2) / 2
    possible_attacks = 2 * (2 * (i - 1) * (i - 2))
    print(int(possible_steps - possible_attacks))
````

## [Two Sets(1092)](https://cses.fi/problemset/task/1092/)
````python
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
````
## [Bit Strings (1617)](https://cses.fi/problemset/task/1617)
````python
n = int(input())
print(2**n % (10**9+7))

````

## [Trailing Zeros (1618)](https://cses.fi/problemset/task/1618/)
````python
# mathematical background: https://www.purplemath.com/modules/factzero.htm
n = int(input())
fact = 1
cnt = 0

while (n // 5**fact) != 0:
    cnt += n // 5**fact
    fact += 1

print(cnt)
````

##[Coin Piles (1754)](https://cses.fi/problemset/task/1754/)
````python
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

##[Creating Strings I (1622)](https://cses.fi/problemset/task/1622/)
````python
from itertools import permutations

n = str(input())
p = permutations(n)
set1 = set()
cnt = 0

for i in p:
    if ''.join(i) not in set1:
        set1.add(''.join(i))
        cnt += 1

set1 = sorted(set1)

print(cnt)
for v in set1:
    print(v)
````

##[Apple Division (1623)](https://cses.fi/problemset/task/1623/)
````python
n = int(input())
p = [int(i) for i in input().split()]

def findMin(arr, n):
    sumTotal = 0
    for i in range(n):
        sumTotal += arr[i]
    return findMinRec(arr, n, 0, sumTotal)

def findMinRec(p, n, sumCalculated, sumTotal):
    if (n == 0):
        return abs((sumTotal - sumCalculated) - 
                   sumCalculated)

    return min(findMinRec(p, n - 1, sumCalculated + p[n - 1], sumTotal), 
               findMinRec(p, n - 1, sumCalculated, sumTotal))


print(findMin(p, n))
````