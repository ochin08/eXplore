

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("You can't divide by zero!")
    return a / b

print(divide(10, 2))  # Works
print(divide(5, 0))   # Raises ZeroDivisionError