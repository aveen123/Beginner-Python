# The key value pair , we use curly brackets to make a dictionary

cats = {"Jane": 6, 
        "Tom": 14,
        "Sara": 8
        }

print(len(cats)) # Printing the length of the dictionary

cats['Wilson'] = 1 # Appending a key value pair into the dictionary
print(cats)

del(cats["Tom"]) # deleting a key value pair inside of the dictionary
print(cats)

print(cats["Sara"]) # printing the value for a specific key---> can only provide key not the value
