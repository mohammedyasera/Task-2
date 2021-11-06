def sum_odd_and_even(l):
    result = []
    evenSum, oddSum = 0,0
    for i in l:
        if i % 2 == 0:
            evenSum += i
        else:
            oddSum += i
    result.append(evenSum)
    result.append(oddSum)
    return result



print(sum_odd_and_even([0,0]))
