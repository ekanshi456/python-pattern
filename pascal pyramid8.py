# input n
n = 7

#this loop is printing for columns
for i in range(1, n + 1):
    for j in range(0, n - i):
        print(' ', end=' ')

    # first element is always 1
    C = 1
    for j in range(1, i + 1):
        # first value in a line is always 1
        print(' ', C, end=' ')

        # using Binomial Coefficient
        C = C * (i - j) // j
    print()