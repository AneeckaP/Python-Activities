string=input("Enter your medical cause.")
attendance=int(input("Enter your attendance."))
if string == "y":
    print("You are allowed.")
else:
    if attendance>=75:
        print("You are allowed.")
    else: 
        print("You are not allowed.")