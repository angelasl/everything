# #This is a comment.
# #Python doesn't read
# #what goes here.
# #Only for Humans!
#
# #prints for Humans!
# print("Hello, World!")
#
# answer= input ("Who inspires you?")
# print(answer, "inspires you!")
#
# #imports the ability to get a random number (we will learn more about this later!)
# from random import *
#
# #Generates a random integer.
# aRandomNumber = randint(1, 20)
# # For Testing: print(aRandomNumber)
#
# guess = input("Guess a number between 1 and 20 (inclusive): ")
# if not guess.isnumeric(): # checks if a string is only digits 0 to 9
# 	print("That's not a positive whole number, try again!")
# else:
# 	guess = int(guess) # converts a string to an integer


# Update this text to match your story.
start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

print(start)

while True:
    print("Type 'left' to go left or 'right' to go right.") # Update to match your story.
    user_input = input()
    if user_input == "left":
        print("You decide to go left and...") # Update to match your story.

    # Continue code to finish story.

    elif user_input == "right":
        print("You choose to go right and ...") # Update to match your story.

    else: print("Try again!")
        # Continue code to finish story.
