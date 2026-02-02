# Code Requirements
# Input: Use any valid input source such as a keyboard, mouse, microphone, data stream, or file.
# Output: Must depend on the input provided.
# List Usage:
# Must justify why a list is better than alternatives.
# Examples include picking items, random selections, or using list methods like append.
# Function Requirements:
# Must have a parameter.
# Include sequencing (multiple lines of code).
# Utilize selection (e.g., if/else statements).
# Use iteration (e.g., loops like for or while).
# Take different paths based on parameter values.


joke = input("Do you want to hear a joke (Yes or No)?: ")


# Defining our Functions
def rate_game():
    rate = int(input("Please rate our game 1-10! "))
    final_score = int(rate * 10)
    print(str(final_score) + " percent satisfaction rate")
    friend = input("Would you recommend this game to a friend? ")

    if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it. ")
    else:
        print("Sorry you did not enjoy it. ")

new=input("Would you like to hear a custom joke?")
    if new= "yes":
        new_subject=input("Tell me a thing")
        new_place=input("Tell me a place")
        create_joke(new_subject,new_place)
        else: 
            print("Bye then!")
def create_joke(subject, place):
    input(f"why did the ", subject, "go to the ", place)
    print("Cause it wanted to duh")
def robber_joke(joke1):
    input("Knock Knock ")
    input("Calder")
    print("Calder police - I've been robbed!")
    joke = input("Do you want to hear another joke or are you finished? ")

def robber_joke(joke2):
    input("hi")
    
def tanks_joke(joke1):
    input("Knock Knock ")
    input("Tank ")       
    input("You are welcome! ")
    joke = input("Do you want to hear another joke or are you finished? ")

def tank_joke(joke2):
    
def pencils_joke(joke1):
    input("Knock Knock ")
    input("Broken pencil ")        
    input("Nevermind, it's pointless! ")
    joke = input("Do you want to hear another joke or are you finished? ")
    
def pencils_joke(joke2):
   
    
if joke == "no".capitalize:
    print("Okay suit yourself")
    rate_jokes() #calls the rating thing when finished

#Main Loop
while joke == "yes".capitalize:
    print("Great, Let's Play")
    question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
    if question == "robbers":
        variety=input(f"Joke 1 or 2?")
        if variety==1:
            robber_joke(joke1)
            else:
            robber_joke(joke2)
    elif question == "tanks".capitalize:
        tanks_joke()
    elif question == "pencils".capitalize:
        pencils_joke()
    if joke == "no".capitalize:
        break


#After we get out of the while loop, this function run
rate_game()