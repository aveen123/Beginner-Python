# Strings can be represented either inside of single or double quotes

shirt = "blue"

print(r"My shirt is " + shirt)

# store = 'Nick's pizza shop' ----? this syntax is incorrect, we cannot have an apostropie inside of the single quote, python assumes that the string ended there, hence use double quotes

store = "Nick's Pizza Shop"

print(store)

store = 'Nick\'s Pizza Shop, the "best" there is' # in order to use quotes inside a quote, we use "\" escape character

print(store)