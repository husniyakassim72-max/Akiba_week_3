# function
def student (name,department):
    print("Name:",name)
    print("Department:",department)
    student("Ali","IT")

def Add(a,b):
    return  a+b   
# return sends a result from a function back to the place where the function was called.
Add(10,9)
def calculate_area(length,width):
    return length*width

length=float(input("Length:"))
Width=float(input("Width:"))
print(calculate_area(length,Width))
# Default Parameters
def greet(name,message="welcome!"):
    print(message,name)
greet("sara")
greet("sara","good morning!")    
# Keyword Arguments
# Keyword arguments mean passing values using parameter names.
def addition (a,b):
    return  a+b
print(addition(12,4))
# Positional Arguments
def rectangle_area(length,width):
    return length*width
area=rectangle_area(10,5)
print(area)
# Variable scoping
# local variable
def calculate_total():
    price=100
    tax=15
    return price+tax
print(calculate_total())
# global variable
tax_rate=0.15
def calculate_tax(price):
    return price*tax_rate
print(calculate_tax(100))
# Function Composition
def get_total(price,tax):
    return price+tax
def print_bill(price,tax):
    total=get_total(price,tax)
    print("Total:",total)
print_bill(100,15)
# calculation eunction
def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def even(a):
    if a%2==0:
        return "even"
    
print(add(2,3))
print(substract(3,1))
print(multiply(2,3))
print(divide(4,3))
print(even(4))

def is_even(number):
    return number%2==0
print(is_even(10))
print(is_even(7))   
    # student grade
def get_grade(score):
    if score>=90:
        return"A"
    elif score>=80:
        return"B"
    elif score>=70:
        return "C"    
    elif score>=60:
        return "D"   

    return "F"
print(get_grade(89))
print(get_grade(67))
print(get_grade(50))
# password validation
def is_valid_password(password):
    return len(password) >= 8

password = input("Password: ")

print(is_valid_password(password))