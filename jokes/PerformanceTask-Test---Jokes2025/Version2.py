#test

joke = input("Do you want to hear a joke (Yes or No)?: ")

# Defining our Functions

def robber_joke():
    input("Knock Knock ")
    input("Calder")
    print("Calder police - I've been robbed!")
    joke = input("Do you want to hear another joke or are you finished? ")
    return 1

def tanks_joke():
    input("Knock Knock ")
    input("Tank ")       
    input("You are welcome! ")
    joke = input("Do you want to hear another joke or are you finished? ")
    return 2

def pencils_joke():
    input("Knock Knock ")
    input("Broken pencil ")        
    input("Nevermind, it's pointless! ")
    joke = input("Do you want to hear another joke or are you finished? ")
    return 3

def rate_game():
    rate = int(input("Please rate our game 1-10! "))
    final_score = int(rate * 10)
    print(str(final_score) + " percent satisfaction rate")
    friend = input("Would you recommend this game to a friend? ")

    if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it. ")
    else:
        print("Sorry you did not enjoy it. ")


#main loop

joke_numeral = [1,2,3]

while joke == "yes":
    
    question = input("Do you want to hear a joke about robbers, tanks, or pencils (1,2,3): ")
    for choice in joke_numeral:
        if choice == 1:
            robber_joke()
        elif choice == 2:
            tanks_joke()
        elif choice == 3:
            pencils_joke()

#when you leave the while loop, this function runs
rate_game()
