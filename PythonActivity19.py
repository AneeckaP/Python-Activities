valid=False
while not valid:
    try:
        n=int(input('Enter a numer: '))
        while n%2==0:

            print("Goodbye!!!!!!!!")
        valid=True
    except ValueError:
        print("Invalid")
       