def seriesSum(n : int) -> int:
    sum = 0
    for i in range(n+1):
        print(i)
        sum += i
        print(sum)
    return sum

print(seriesSum(3))