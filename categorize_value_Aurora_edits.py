'''Lab 7. The first 3 lines are the solution from the Vocareum lab (although I changes the value). 
I decide to present the data by type in a more human readable format'''
myMixedBagList = [42, 1963, 10001011, True, "Yo!", "42", 3.14159]
for item in myMixedBagList:
    print("{} is of data type{}.".format(item,type(item)))
# Define variables for the data type lists with empty lists
integers = []
strings = []
booleans = []
floats = []
#This is a for loop using string method that iterates through the items in the myMixedBaglist to add items to the appropriate list.
for item in myMixedBagList:
    if type(item) == int:
        integers.append(item)
    if type(item) == str:
        strings.append(item)
    if type(item) == bool:
        booleans.append(item)
    if type(item) == float:
        floats.append(item) 
#Print the each list with a string identifying the data type.
print("These items are integers: {}".format(integers))
print("These items are strings: {}".format(strings))
print("These items are boolean: {}".format(booleans))
print("These items are floats: {}".format(floats))