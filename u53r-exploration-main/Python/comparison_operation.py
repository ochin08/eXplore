



# 1. Equal to (==) - Sinusuri kung pantay ang dalawang halaga
print(5 == 5)     # True
print("apple" == "orange")  # False

# 2. Not equal to (!=) - Sinusuri kung hindi pantay ang dalawang halaga
print(10 != 5)    # True
print("hello" != "hello")  # False

# 3. Greater than (>) - Sinusuri kung mas malaki ang unang halaga kaysa sa pangalawa
print(7 > 3)      # True
print(2 > 8)      # False

# 4. Less than (<) - Sinusuri kung mas maliit ang unang halaga kaysa sa pangalawa
print(4 < 10)     # True
print(5 < 3)      # False

# 5. Greater than or equal to (>=) - Mas malaki o pantay
print(6 >= 6)     # True
print(9 >= 5)     # True
print(4 >= 7)     # False

# 6. Less than or equal to (<=) - Mas maliit o pantay
print(3 <= 5)     # True
print(10 <= 10)   # True
print(8 <= 4)     # False

# 7. Identity Operators - Paghahambing ng "identity" sa memory (is, is not)
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # True (pareho ang reference sa memory)
print(a is c)      # False (magkapareho ang value pero magkaibang object)
print(a is not c)  # True

# 8. Membership Operators - Paghahanap ng elemento sa loob ng sequence (in, not in)
fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)      # True
print("grape" in fruits)      # False
print("mango" not in fruits)  # True

# 9. Boolean Comparisons - Paghahambing ng True at False
print(True == 1)   # True
print(False == 0)  # True
print(True > False)  # True (1 > 0)
print(False < True) # True (0 < 1)
