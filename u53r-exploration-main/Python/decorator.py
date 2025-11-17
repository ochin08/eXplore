




# Simpleng decorator
def simple_decorator(func):
    def wrapper():
        print("Bago tawagin ang function.")
        func()
        print("Pagkatapos tawagin ang function.")
    return wrapper

# Gamitin ang decorator sa function
@simple_decorator
def greet():
    print("Hello, mundo!")

# Tawagin ang decorated function
greet()
