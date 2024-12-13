#Functions
#Example 1
def greet():
  print("Hello, Welcome to the Python world!")
greet()

#Exampl 2 
def greet_person(name):
    print(f"Hello, {name}! kaisi ho?")

greet_person("Shiza")

#Example 3
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return "Invalid operation"

result = calculator(10, 20, "divide")
print(f"Result is: {result}") 

#Example 4
def get_greeting():
    return "Welcome to Python!"

print(f"{get_greeting()} Shiza!")

