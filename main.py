def simpleArraySum(ar):
    summ = 0  
    for n in ar:
        summ = n + summ 
    print(summ)
    return summ



simpleArraySum([1, 2, 3, 4, 5])         #15
simpleArraySum([1, 2, 3, 4, 5, 10])     #25
simpleArraySum([1, 2, 3, 4, 5, 10, 12])     #37