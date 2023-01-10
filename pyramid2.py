n = 5
for i in range(0, n):
    for j in range(0, n-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print(" *",end=" ")
    print()

# Inverted Program

# using for no of rows
n = 5

# this loop is to print rows
for i in range(n, 0, -1):

    # this inner loop is to print space
    for j in range(0, n - i):
        print(end=" ")

    # this inner loop is to print star
    for j in range(0, i):
        print("* ", end=" ")

    # after every iteration the next iteration will be printed in new line
    print()


