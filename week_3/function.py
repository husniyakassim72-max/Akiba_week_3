def greet(name):
    print("hello world",name)

greet("ahmed")
greet("sara")
def profile(my_name,age=16,city="unknown"):
    print(my_name,age,city)

profile("Ali",22,"jimma")    
def is_valid_password(password):
        return len(password)>=8

print    (is_valid_password("hello"))
print(is_valid_password("hello123"))