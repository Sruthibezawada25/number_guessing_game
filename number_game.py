import random

print("🎯 Welcome to Number Matching Game!")
print("I have selected a number between 1 and 100. Can you guess it?")

number = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("Enter your guess: "))
    tries += 1

    if guess < number:
        print("Your guess is too small! 📉")
    elif guess > number:
        print("Your guess is too big! 📈")
    else:
        print(f"🎉 Correct! You guessed the number in {tries} tries.")
