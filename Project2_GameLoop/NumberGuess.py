import random
import time

print("Hi!")
time.sleep(2)
print("WELCOME TO THE NUMBER GUESSING GAME!")
time.sleep(1)
print("I am going to pick a number between 1 and 100.")
time.sleep(1)
print("Picking a number....")
time.sleep(2)
guess = int(input("What is your guess?: "))

correct_number = random.randint(1, 100)
guess_count = 1

print("Checking if your guess is correct.......")
time.sleep(2)

while guess != correct_number:
    time.sleep(1)
    guess_count +=1

    if guess < correct_number:
        guess = int(input("Sorry, your guess is incorrect. Guess HIGHER!: "))
    
    elif guess > correct_number:
        guess = int(input("Sorry, your guess is incorrect. Guess LOWER!: "))
    
    print("Checking if your guess is correct.......")
    time.sleep(2)

time.sleep(1) 
print(f"Congrats! The right answer was {correct_number}. It took you {guess_count} guesses.")