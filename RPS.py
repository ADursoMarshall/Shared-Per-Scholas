# Rock, paper, scissors to practice defining functions and more loops
# We will need to import random to choose R,P,S for the computer

options = ["rock", "paper", "scissors"] #This variable was giving me some trouble so it is all over the place.
#define function to randomly select for the computer.
def comp():
    import random
    options = ["rock", "paper", "scissors"]
    pos = random.randint(0,2)
    compA = options[pos]
    return compA 

# define function to get user input
def chal(): 
    challenger = input("Choose rock, paper, or scissors: ")
    challenger = challenger.lower()
    return challenger

# main game function
def game():
    #defime additional variables
    yWin = "You Win!"
    yLose = "Sorry, better luck next time."
    notValid = True
    count = 0
    options = ["rock", "paper", "scissors"]
    #call the functions for computer and user selections
    compB = comp()
    chalA = chal()
    #loop to verify that the user input is valid, and kicks out after three invalid entries
    while notValid == True:
        if chalA in options:
            notValid = False
        elif count < 3:
            chalA = chal()
            count = count +1
        else:
            print("We can play later.")
    #This loop ensures there is no tie by haveing the computer selection loop if it matches the user input
    while compB == chalA:
        compB = comp()
    
    print("Your opponent selected:", compB)
    #Win/loss conditions
    if compB == "rock" and chalA == "scissors":
        outCome = yLose
    elif compB == "rock" and chalA == "paper":
        outCome = yWin
    elif compB == "paper" and chalA == "scissors":
        outCome = yWin
    elif compB == "paper" and chalA == "rock":
        outCome = yLose
    elif compB == "scissors" and chalA == "rock":
        outCome = yWin
    elif compB == "scissors" and chalA == "paper":
        outCome = yLose
    print(outCome)
    #LOOK IT'S RECURSIVE!! 
    again = input("would you like to play again? (yes or no): ")
    again = again.lower()
    if again == "yes":
        game()
    else:
        print("Ok, Goodbye.")
#Start of the program        
play = input("Would you like to play a game? (type yes or no): ")
play = play.lower()
if play == "yes":
    game()
else:
    print("Ok, goodbye.")
