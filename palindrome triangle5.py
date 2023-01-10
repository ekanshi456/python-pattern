# using for no of rows
n = 7

# this loop is for printing rows
for i in range(1, n):

    # this is for printing first half of palindrome
    for j in range(1, i + 1):
        # printing single blank spaces
        print(j, end="")

    # this is for negative Updation
    for k in range(j - 1, 0, -1):
        # printing decrement numbers
        print(k, end="")

        # after every iteration the next iteration will be printed in new line
    print()

#Inverted Pattern

# using for no of rows
n = 7

# this loop is for printing rows
for i in range(1, n):

    #this is to print blank space before first palindrome
    for j in range(n - 1 - i):
        print(" ", end=" ")

    # this is for printing first half of palindrome
    for j in range(1, i + 1):
        print(j, end="")

    # this is for negative Updation
    for k in range(j - 1, 0, -1):
        # printing decrement numbers
        print(k, end="")

        # after every iteration the next iteration will be printed in new line
    print()



