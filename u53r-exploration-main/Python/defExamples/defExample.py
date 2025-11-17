
#1
def greet():
    print("Hello, world!")

greet()  # First call
greet()  # Second call


#2
name = input("Enter your name: ")
def greet(name):
    print("Hi!" + name)
    print("Hello!" + name)
    print("How are you?" + name)

greet(name + " ")