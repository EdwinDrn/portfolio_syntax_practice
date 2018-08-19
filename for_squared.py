#This program shows different ways of how to take a number, square it for a range given.
#Then we are able to print the output in either brackets, or a list.
#We also loop through a function as well.

#Program Prints Squared numbers begining with the number 1, in brackets.

even_squares = [x * x for x in range(1, 11)]


for x in range(1, 11):
    x = x * x
    print x

def even_squares_function():
    for x in range(1, 100):
        print x * x

print even_squares
even_squares_function()
