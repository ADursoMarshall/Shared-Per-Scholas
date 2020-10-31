# This is lab 6 exercise 2. Creating a for loop. I added a while/if/else, so they user could choose a number.
print("We are going to count." )
outOfRange = True #define a boolean variable for in put out of the instructed range.
while outOfRange == True:
    count = input ("How high would you like to count? (Pick a number between one and twenty): ") 
    if int(count) > 20 or int(count) <1:
        print("Hmm, that won't work. Pick a number between 1 and 20; ")
        outOfRange = True
    else:
        print("Okay, Lets count to {}".format(count))
        outOfRange = False
        for x in range(1,(int(count)+1)):
            print (x)