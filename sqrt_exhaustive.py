# We need an integer, converting string to int
x = int(input("Enter a positive integer: "))
guess=0

#Checking to see whether the integer has a square or not
while guess**2 < x:
    guess = guess + 1
if guess**2 == x:
    print("Square root of {} is {}".format(x, guess))
else:
    print("No sqare root found for {}".format(x))
#This is a change