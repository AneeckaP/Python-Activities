answer= int(input("Do you need to shut down your computer"))
if answer=="Yes" or "yes":
    print("Your computer will shut down in 5 second")
    import os
    os.system("shutdown /s /t 5") 
else:
    print("Your computer will not be shut down")
    