
#1
# Lambda function to add two numbers
add = lambda x, y: x + y

# Gamitin ang lambda function
result = add(5, 3)
print(result)  # Output: 8



#2 Map
# Gusto nating i-multiply ng 2 ang bawat numero sa list
numbers = [1, 2, 3, 4]
result = map(lambda x: x * 2, numbers)
print(list(result))  # Output: [2, 4, 6, 8]


#3 Filter
# Keep only even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6]


#3 Sorted
# Sort a list of tuples by the second value
pairs = [(1, 3), (2, 2), (4, 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Output: [(4, 1), (2, 2), (1, 3)]
