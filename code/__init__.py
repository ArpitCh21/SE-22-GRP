import random
a = random.randint(1, 20)
i = 0
print("Between 1 and 20, Guess the number I am thinking right now! You have 3 chances")
while i < 3:
    guess = int(input(f"Chance {i+1}: "))
    if guess < a:
        print("Your guess is smaller!")
    elif guess > a:
        print("Your guess is greater!")
    else:
        print("You win!")
        break
    i += 1
else:
    print(f"""You have used all your chances. You Lose!
Correct number was {a}""")

# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))

# operator = input("Type operator: ")

# if operator == "+":
#     print("Addition is: ", num1+num2)
# elif operator == "-":
#     print("Subtraction is: ", num1-num2)
# elif operator == "*":
#     print("Multiplication is: ", num1*num2)
# elif operator == "/":
#     print("Division is: ", num1/num2)
# else: print("Please choose correct operator.")
