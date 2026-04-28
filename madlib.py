# A simple Mad Libs game in Python

print("Welcome to the Python Mad Libs Generator!")

# Get input from the user for different parts of speech
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
place = input("Enter a place: ")

# Create the story using f-string formatting
story = f"""
Today I went to the {adjective} {place}. 
I saw a {noun} trying to {verb}. 
It was the most unforgettable day ever!
"""

# Print the final story
print("\\nHere is your Mad Lib story:")
print(story)
