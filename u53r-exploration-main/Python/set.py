

#
#1
nums = {1, 2, 3, 4, 5}
print(nums)
nums.add(-6)
nums.remove(2)
print(nums)
print(len(nums))



#2
#Union Operator (Pagsamahin lahat ng laman ng dalawang set, walang ulit (unique lang).)
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # Output: {1, 2, 3, 4, 5}


# Intersection Operator (Kunin lang yung mga common o magkapareho sa dalawang set.)
a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)  # Output: {3}


# Difference Operator (Kunin yung mga nasa unang set lang pero wala sa pangalawa.)
a = {1, 2, 3}
b = {3, 4, 5}
print(a - b)  # Output: {1, 2}


# Symmetric Difference Operator (Kunin yung mga nasa alinman sa dalawang set, pero hindi parehong meron.)
a = {1, 2, 3}
b = {3, 4, 5}
print(a ^ b)  # Output: {1, 2, 4, 5}
