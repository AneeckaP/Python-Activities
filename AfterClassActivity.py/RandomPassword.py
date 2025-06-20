import random
import string
def generate_random_password(length=7):
    characters=string.ascii_lowercase+string.ascii_uppercase+string.digits
    password_list=[random.choice(characters) for i in range(length)]
    random.shuffle(password_list)
    return "".join(password_list)

password=generate_random_password()
print(f"Generated Password: {password}")