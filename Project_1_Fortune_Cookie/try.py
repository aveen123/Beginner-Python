# Make your own version of a magic 8 ball that prints yes, no, or maybe each time you ask it

import random

answer = random.randint(1, 3)

if answer == 1:
    print("Yes")
elif answer == 2:
    print("No")
else:
    print("Maybe")