import json

# Make a list of questionss
questions = [
"What's your name?",
"What is your favorite genre of music?",
"What is your favorite color?",
"How many siblings do you have?",
"What kind of phone do you have?"]

# Make a list of keys
keys = ["name","genre","color", "siblings", "phone"]

# Make a list of answers
listAnswers =[]

done= "no"
while done =="no":
# Creates the dictionary to store responses.
    answers = {}

    print("New Entry, please respond to the questions:")
    for x in range(len(questions)):
        response = input(questions[x] + " ")
        answers[keys[x]] = response

    listAnswers.append(answers)

    done =  input("Are you the last person?").lower()
# Print the context of the dictionary.
print(listAnswers)

with open('data.json', 'w') as f:
    json.add(listAnswers, f)
