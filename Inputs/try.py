# First ask for some text, and then prompt "Enter 1 to uppercase and 2 to lowercase: " and then either uppercase or lowercase it

userText = input("Enter some text: ")
userChosen = int(input("Enter 1 to uppercase or 2 to lowercase: "))

if userChosen == 1:
    print(userText.upper())
if userChosen == 2:
    print(userText.lower())