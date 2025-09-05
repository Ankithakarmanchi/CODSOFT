import random
import string
run_again='y'
while run_again.lower()=='y':
    try:
        password_length=int(input("Enter the desired password length:"))
        characters=string.ascii_letters+string.digits+string.punctuation
        password=""
        for i in range(password_length):
            password+=random.choice(characters)
        print("Generated password:",password)
    except ValueError:
          print("Invalid input:Please enter a valid number(integer) for the password length")
    run_again=input("Do you wanna generate another password, if yes enter y else n?(y/n):")
print("\nthank you for using password generator...! \n keep doing, All the best\n")
