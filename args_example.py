#This program takes arguments and adds them together. (These are arguments that are provided up front)
#7/30/2020, Written by Edwin Duran

def sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result

list_of_integers = [1, 2, 3, 4]
print (sum(list_of_integers))


#Example using *args

def user_sum(args):
    results = 0
    for y in args:
        results += y
    return results

user_numbers = [2, 2, 2, 2, 2, 3]
print (user_sum(user_numbers))
