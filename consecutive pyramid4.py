#using for no of rows
n = 6
num = 1
col = 1
for i in range(1,n):
    for j in range(n - i):
        print(" ",end="  ")
    for j in range(1,col+1):
        print(num, end="  ")
        num = num+1
    col = col + 2
    print()






