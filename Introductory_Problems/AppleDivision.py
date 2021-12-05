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