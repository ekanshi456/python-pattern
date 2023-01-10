# # using for no of rows
# n = 7
#
# # this loop is for printing rows
# for i in range(1, n):
#
#     # this loop is using for blank space
#     for j in range(1, n + 1 - i):
#         print(' ', end=' ')
#
#     # this loop,is using for increase the pattern
#     for j in range(1, i + 1):
#         print(j, end=" ")
#
#         # this loop is using for negative updation(decreasing)
#     for k in range(j - 1, 0, -1):
#         print(k, end=" ")
#         # after every iteration the next iteration will be printed in new line
#     print()


# using for no of rows
n = 7

# this loop is for printing rows
for i in range(1, n):

    # this loop is using for blank space
    for j in range(n + 1 - i):
        print(' ', end=' ')

    # this loop,is using for increase the pattern
    for j in range(1,i + 1):
        print(j, end=" ")

        # this loop is using for negative updation
    for k in range(j - 1, 0, -1):
        print(k, end=" ")
        # after every iteration the next iteration will be printed in new line
    print()

