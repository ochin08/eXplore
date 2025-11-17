


#The code below is part of the program for a vending machine.

products = ["juice", "chocolate", "water"]
user_choice = int(input("Choose a product (0-2): "))
print(products[user_choice])



# Strings are immutable 
word = "car"
word[2] = "t"

#Lists are mutable 
words = ["car", "dog", "bird"] 
words[0] = "cat" 
print(words)


#logic
x = "arctic"
print(x[2] + x[0] + x[3])