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
