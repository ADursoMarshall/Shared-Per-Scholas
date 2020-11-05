#While loop to produce the first 10 numbers of the Fibonacci sequence
fibX = [1, 1, ]

count=2
while count < 10:
    fibX.append(fibX[-1] + fibX[-2])
    count = count +1
print(fibX)