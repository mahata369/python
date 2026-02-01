#Guess the number game v1

# import random

# secret_number = random.randint(1,100)
# attempts = 0

# print("Welcome to Guess The Number Game!")
# print("I have selected a number between 1 and 100.")
# print("Try to guess it")

# while True:
#     guess =int(input("\nEnter your guess:"))
#     attempts += 1

#     if guess > secret_number:
#         print("Too high! Try again.")
#     elif guess < secret_number:
#         print("Too low! Try again.")
#     else:
#         print(f"Congratulations buddy! You guessed it in {attempts} attempts.")
#         break

#Guess the number game v2

# import random

# print("Welcome to the Guess The Number Game v2!")

# while True:
#     secret_number = random.randint(1,100)
#     attempts = 0
    
#     print("\nI have selected a number between 1 and 100")
#     print("Try to guess it")

#     while True:
#         user_input = input("\nEnter your guess:")

#         #Input validation
#         if not user_input.isdigit():
#             print("Please enter a valid number!")

#         guess = int(user_input)
#         attempts += 1

#         if guess > secret_number:
#             print("Too high!Try again.")
#         elif guess < secret_number:
#             print("Too low! Try again.")
#         else:
#             print(f"congratulations buddy! you guess it in {attempts} attempts")
#             break

#     play_again = input("\n Do you want to play again?")
#     if play_again != "y":
#         print("Bye buddy! Take care")
#         break

#Guess the number game v3
import random

def choose_difficulty():
    print("\nChoose Difficulty:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200,5 attempts)")

    while True:
        choice = input("Enter 1/2/3: ")
        if choice == "1":
            return 50,10,"Easy"
        elif choice == "2":
            return 100, 7, "Medium"
        elif choice =="3":
            return 200, 5, "Hard"
        else:
            print("Invalid choice. Please enter 1,2 or 3.")

def get_valid_guess(Prompt):
    while True:
        value = input(Prompt)
        if value.isdigit():
            return int(value)
        else:
            print("Please enter a valid number!")

print("Welcome to Guess The Number Game v3!")

while True:
    max_range, max_attempts, difficulty = choose_difficulty()
    secret_number = random.randint(1, max_range)

    attempts = 0
    print(f"\n Difficulty: {difficulty}")
    print(f"I have selected a number between 1 and {max_range}.")
    print(f"You have {max_attempts} attempts. Good luck")

    won = False

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        print(f"\n Attempts left: {remaining}")

        guess =get_valid_guess("Enter your guess: ")

        if guess > secret_number:
            print(" Too high!")
        elif guess < secret_number:
            print(" Too low!")
        else:
            print(f"\n Congratulations! You guessed it in {attempts} attempts.")
            won = True
            break
    if not won:
        print("\n Game over!")
        print(f"The correct number was: {secret_number}")

    play_again =input("\nDo you want to play again?")
    if play_again != "y":
        print("Bye! See you next time")
        break