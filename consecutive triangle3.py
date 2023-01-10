# It is also called floyd's triangle

# using for no of rows
n = 5

#
num = 1

# this loop is to print rows
for i in range(0, n + 1):

    # this loop is to print columns
    for j in range(0, i):
        print(num, end=" ")

        # this is for increasing numbers
        num = num + 1

        # after every iteration the next iteration will be print in new line
    print()

# invert pattern

# using for no of rows
n = 5

#
num = 15

# this loop is to print rows
for i in range(0, n):

    # this loop is to print columns
    for j in range(n - i):
        print(num, end=" ")

        # this is for decreasing numbers
        num = num - 1

        # after every iteration the next iteration will be print in new line
    print()
