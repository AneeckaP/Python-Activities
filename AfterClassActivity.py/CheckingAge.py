def check_age():
    while True:
        try:
            age_str = input("Enter your age: ")
            age = int(age_str)
            if age < 0 or age > 150:
                print("Invalid age. Please enter an age between 0 and 150.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer for age.")
    
    if age % 2 == 0:
        print(f"{age} is an even number.")
    else:
        print(f"{age} is an odd number.")

check_age()