rows= int(input("Enter the number of rows you want in your triangle:"))
print("Here is your Floyd's Triangle for your", rows,"rows")
number=1
for num in range (rows):
    for j in range (num+1):
        print(number, end =" ")
        number =(number+1)
    print ()
