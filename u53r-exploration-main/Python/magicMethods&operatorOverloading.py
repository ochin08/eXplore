



# Magic Methods
class A:
    def __init__(self, value):
        self.value = value

    def __str__(self):  # Para sa print()
        return f"A({self.value})"

    def __add__(self, other):  # Para sa +
        return A(self.value + other.value)

a1 = A(10)
a2 = A(20)
a3 = a1 + a2
print(a3)  # Output: A(30)




#Overloading Operators
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # + operator
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):  # print output
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3)  # Output: Point(4, 6)
