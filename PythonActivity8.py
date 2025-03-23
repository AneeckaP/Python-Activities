rows=int(input("Enter the number of rows: "))
print("The triangle which you want to print has", rows ," rows")
for i in range (rows):
    for j in range (i+1) :
        print("*", end=" ")
    print ()


