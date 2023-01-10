for i in range(0, 7):
    x = 1
    for j in range(1, 7-1):
        print("", end="")

    for k in range(0, i + 1):
        print(" ", x, end="")
        x = int(x * (i-k) / (k + 1))
    print()

#
# for i in range(0, 7):
#     x = 1
#     for j in range(0,7-1):
#         print("", end="")
#
#     for k in range(7-1-i,0,-1):
#         print(" ", x, end="")
#         x = int(x * (i+k) / (k + 1))
#     print()

# input n
n = 7

#this loop is printing for columns
# for i in range(1, n + 1):
#
#     # first element is always 1
#     C = 1
#     for j in range(1, i + 1):
#         # first value in a line is always 1
#         print(' ', C, end=' ')
#
#         # using Binomial Coefficient
#         C = C * (i - j) // j
#     print()


