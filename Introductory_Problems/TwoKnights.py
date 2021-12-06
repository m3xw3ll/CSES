n = int(input())

for i in range(1,n+1,1):
    possible_steps = (i**4 - i**2) / 2
    possible_attacks = 2 * (2 * (i - 1) * (i - 2))
    print(int(possible_steps - possible_attacks))