# Rock, paper, scissors to practice defining functions and more loops
# We will need to import random to choose R,P,S for the computer

options = ["rock", "paper", "scissors"]
def comp():
    import random
    options = ["rock", "paper", "scissors"]
    pos = random.randint(0,2)
    compA = options[pos]
    return compA 


# Get user input
def chal(): 
    challenger = input("Choose rock, paper, or scissors: ")
    challenger = challenger.lower()
    return challenger


def game():
    compB = comp()
    chalA = chal()
    yWin = "You Win!"
    yLose = "Sorry, better luck next time."
    notValid = True
    count = 0
    options = ["rock", "paper", "scissors"]
    while notValid == True:
        if chalA in options:
            notValid = False
        elif count < 3:
            chalA = chal()
            count = count +1
        else:
            print("We can play later.")

    while compB == chalA:
        compB = comp()
    
    print("Your opponent selected:", compB)

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
    
    again = input("would you like to play again? (yes or no): ")
    again = again.lower()
    if again == "yes":
        game()
    else:
        print("Ok, Goodbye.")
        
play = input("Would you like to paly a game? (type yes or no): ")
play = play.lower()
if play == "yes":
    game()
else:
    print("Ok, goodbye.")

