#EXERCISE 1
def add_two_numbers (x,y):
    return (x+y)

print(add_two_numbers(3, 5))
print(add_two_numbers(10, 20))

#EXERCISE 2
def greet (name):
    return f'Hello, {name}'

print (greet("Alice"))
print (greet("Bob"))

#EXERCISE 3
def check_even_odd (x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(check_even_odd(4))
print(check_even_odd(7))

#EXERCISE 4
def sum_list (numbers):
    return sum(numbers)

print(sum_list([1, 2, 3, 4]))
print(sum_list([5, 5, 5]))

#EXERCISE 5
def print_days():
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    for day in days:
        print(day)

print_days()

#EXERCISE 6
def check_sign(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print(check_sign(10))  
print(check_sign(-15))  
print(check_sign(0))  


#EXERCISE 7
def repeat_word(word, number):
        for number in range(number):
            print(word)

print(repeat_word("hello", 3))
print(repeat_word("goodbye", 2))