#This is a little bit of code to select a randon string from a list of strings(could be used for any data in a list)
import random #this is an imported function fro random numbers
myFruitList = ["apple", "orange", "pineapple", "cherry"] #list of strings
lastPos = (len(myFruitList)-1)

pos = random.randint(0,lastPos)
print(myFruitList[pos])