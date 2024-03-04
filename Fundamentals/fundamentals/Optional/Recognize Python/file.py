num1 = 42  # variable declaration - Numbers initialized
num2 = 2.3  # variable declaration - Numbers initialized
boolean = True  # variable declaration - Boolean initialized
string = 'Hello World'  # variable declaration - Strings initialized
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  # Composite Data Types - List (initialize)
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  # Composite Data Types - Dictionary (initialize)
fruit = ('blueberry', 'strawberry', 'banana')  # Composite Data Types - Tuples (initialize)
print(type(fruit))  # type check - Primitive Data Types

print(pizza_toppings[1])  # access value - List
pizza_toppings.append('Mushrooms')  # add value - List
print(person['name'])  # access value - Dictionary
person['name'] = 'George'  # change value - Dictionary
person['eye_color'] = 'blue'  # add value - Dictionary
print(fruit[2])  # access value - Tuples

if num1 > 45:  # conditional - if
    print("It's greater")
else:  # conditional - else
    print("It's lower")

if len(string) < 5:  # length check
    print("It's a short word!")
elif len(string) > 15:  # conditional - else if
    print("It's a long word!")
else:  # conditional - else
    print("Just right!")

for x in range(5):  # for loop - sequence
    print(x)
for x in range(2,5):  # for loop - start, stop
    print(x)
for x in range(2,10,3):  # for loop - start, stop, increment
    print(x)
x = 0
while(x < 5):  # while loop - start, stop
    print(x)
    x += 1

pizza_toppings.pop()  # delete value - List
pizza_toppings.pop(1)  # delete value - List

print(person)  # log statement
person.pop('eye_color')  # delete value - Dictionary
print(person)  # log statement

for topping in pizza_toppings:  # for loop - sequence
    if topping == 'Pepperoni':  # conditional - if
        continue
    print('After 1st if statement')
    if topping == 'Olives':  # conditional - if
        break

def print_hello_ten_times():  # function - parameter
    for num in range(10):  # for loop - sequence
        print('Hello')

print_hello_ten_times()  # function - argument

def print_hello_x_times(x):  # function - parameter
    for num in range(x):  # for loop - sequence
        print('Hello')

print_hello_x_times(4)  # function - argument

def print_hello_x_or_ten_times(x = 10):  # function - parameter
    for num in range(x):  # for loop - sequence
        print('Hello')

print_hello_x_or_ten_times()  # function - argument
print_hello_x_or_ten_times(4)  # function - argument