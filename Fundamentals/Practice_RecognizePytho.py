num1 = 42     #variable declaration, Data Types:numbers
num2 = 2.3    #variable declaration, Data Types:numbers
boolean = True  #variable declaration, Data Types:boolean
string = 'Hello World'    #variable declaration, Data Types:strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #variable declaration, Composite list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, Dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, Composite tuples
print(type(fruit))      #log statement, type check
print(pizza_toppings[1])    #log statement, access value
pizza_toppings.append('Mushrooms')  #change value
print(person['name'])   #log statement
person['name'] = 'George'   #variable declaration
person['eye_color'] = 'blue'  #variable declaration
print(fruit[2])    #log statement, access value

if num1 > 45:    #conditional if
    print("It's greater")   #log statement
else:           #conditional else
    print("It's lower")   #log statement

if len(string) < 5:   #conditional if
    print("It's a short word!")    #log statement
elif len(string) > 15:  #conditional else if
    print("It's a long word!")   #log statement
else:               #conditional else
    print("Just right!")    #log statement

for x in range(5):    #for loop
    print(x)    #log statement
for x in range(2,5):  #for loop
    print(x)    #log statement
for x in range(2,10,3):  #for loop
    print(x)    #log statement
x = 0
while(x < 5):    #while loop
    print(x)    #log statement
    x += 1   #increment

pizza_toppings.pop()   #function without parameter
pizza_toppings.pop(1)  #function with parameter

print(person)   #log statement
person.pop('eye_color')     #deletevalue
print(person)   #log statement

for topping in pizza_toppings:  #for loop
    if topping == 'Pepperoni':  #conditional if
        continue
    print('After 1st if statement') #log statement
    if topping == 'Olives':   #conditional if
        break

def print_hello_ten_times():   #function 
    for num in range(10):       #for loop
        print('Hello')  #log statement

print_hello_ten_times()   #function without parameter

def print_hello_x_times(x):         #function 
    for num in range(x):          #for loop
        print('Hello')  #log statement

print_hello_x_times(4)       #function with parameter

def print_hello_x_or_ten_times(x = 10):         #function
    for num in range(x):         #for loop
        print('Hello')  #log statement

print_hello_x_or_ten_times()          #function without parameter
print_hello_x_or_ten_times(4)           #function with parameter


"""
Bonus section        # comment multiline
"""

# print(num3)    # comment single line
# num3 = 72      # comment single line
# fruit[0] = 'cranberry'         # comment single line
# print(person['favorite_team'])         # comment single line
# print(pizza_toppings[7])       # comment single line
#   print(boolean)       # comment single line
# fruit.append('raspberry')      # comment single line
# fruit.pop(1)       # comment single line