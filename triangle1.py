def pypart(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("*", end=" ")
        print("")


n = 5
pypart(n)
print()

# Inverted Program

# #using for no of rows
n = 5

# this loop is for printing rows
for i in range(n, 0, -1):

    # this loops is for printing columns
    for j in range(0, i):
        # for printing star
        print("*", end=" ")

    # after every iteration the next iteration will be printed in new line
    print()
