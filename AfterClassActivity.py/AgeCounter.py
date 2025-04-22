try:
    num = int(input("Enter an integer: "))
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")
except ValueError:
    print("Invalid input. Please enter an integer.")