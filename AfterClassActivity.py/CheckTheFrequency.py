test_dictionary = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}
print(test_dictionary)

user_value = input("Enter the value to check its frequency: ")

frequency = 0
for value in test_dictionary.values():
    if str(value) == user_value:
        frequency += 1

print(f"The frequency of {user_value} is: {frequency}")