#Main Version

joke = input("Do you want to hear a joke (Yes or No)?: ").lower()

#this list 
jokes_told = []

# Defining our Functions

def robber_joke():
    input("Knock Knock ")
    input("Calder")
    print("Calder police - I've been robbed!")
    #this return statement is used so that it can be used later on to see if the person wants to hear a joke. If its not yes
    #then it will get us out of the loop down in the program.
    return input("Do you want to hear another joke or are you finished? ").lower()

def tanks_joke():
    input("Knock Knock ")
    input("Tank ")       
    input("You are welcome! ")
    return input("Do you want to hear another joke or are you finished? ").lower()

def pencils_joke():
    input("Knock Knock ")
    input("Broken pencil ")        
    input("Nevermind, it's pointless! ")
    return  input("Do you want to hear another joke or are you finished? ").lower()

def rate_game(jokes_told):
    total = len(jokes_told) 
    rate = int(input("Please rate our game 1-10! "))
    final_score = int(rate * 10)
    print(str(final_score) + " percent satisfaction rate")
    print(f'you were told {total} jokes')
    friend = input("Would you recommend this game to a friend? ").lower()

    if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it. ")
    else:
        print("Sorry you did not enjoy it. ")


#main loop

while joke == "yes":
    
    #This input is used later so that we can track which joke you want to hear
    choices = input("Do you want to hear a joke about robbers, tanks, or pencils (1,2,3)?: ")

    #each joke will play depending on the number that was picked. As well, the joke variable is used later for
    #when the user no longer wants to hear the joke, it will get them out of the loop then plays our rate game function
    
    if choices == '1':
        joke = robber_joke()
        jokes_told.append(1)
    elif choices == '2':
        joke = tanks_joke()
        jokes_told.append(1)
    elif choices == '3':
        joke = pencils_joke()
        jokes_told.append(1)

#when you leave the while loop, this function runs
rate_game(jokes_told)
