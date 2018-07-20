start= "In a far away kingdom, there lived three orphan royals. Two twin sisters and an older brother named Timothy. You are the combined minds of the two sisters. You are plotting to kill Timothy to fight for the throne."
print (start)

#one
print ("Do you want to choose the villager or poison. Type 'villager' or 'poison' to choose")
user_input = input()

#one.1
if user_input == "villager":
    print ("You have two villagers to choose from: Elzabeth and Mary. Elizabeth is a 16 year old who needs the money to care for her younger siblings. Mary is a 20 year old who is expecting. Type 'Elizabeth to choose Elizabeth or''Type Mary to choose Mary'")
user_input = input()

#one.1.1
if user_input == "Elizabeth":
    print ("Should Elizabeth kill Tim while he is sleeping or awake? Type 'sleeping'or 'awake'.")

#one.1.1.1
user_input = input()
if user_input == "sleeping":
    print ("Tim sleep walks and runs away. FAIL! Game over.")

#one.1.1.2
if user_input == "awake":
    print ("Elizabeth wasn't as sneaky as she thought and got killed by a knights")


#one.1.2
user_input= input()
if user_input == "Mary":
    print ("Will Mary risk her and her future son's life? 'Type yes or no' ")
user_input = input()

#one.1.2.1
if user_input == "yes":
    print ("Mary got caught and is sent to prison until she has her baby")

#one.1.2.2

elif user_input == "no":
    print ("Mary stays safe but still lives in the slums")
else: print: "Not a valid choice. Try again."

#two.1
user_input = input()
if user_input == "poison":
    print ("Do you want to kill him slowly over a week or instantly? Type 'slowly'or 'instantly'. ")

#two.1.2
user_input = input()
if user_input == "instantly":
    print ("Do you want to put the poison in steak or pizza? Type 'steak' or 'pizza'. ")
