#Created by aurora.d.marshall@gmail.com
#While loop to produce the first 10 numbers of the Fibonacci sequence.

#Initialize 
fibX = [1, 1, ]

count=2
while count < 10:
    fibX.append(fibX[-1] + fibX[-2])
    count = count +1
print(fibX)

#To find the value at any position in the sequence:

#Initialize 
fibX = [1, 1, ]

#Get user input for the position in the sequence:
#initialize the value
place = 0

# While look to make sure the input is valid
while place < 1:
    place = input("Enter a interger greater than zero: ")
    place = int(place)

count=2
while count < place:
    fibX.append(fibX[-1] + fibX[-2])
    count = count +1
print(fibX[-1])

# Need to add a string to the output