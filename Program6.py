# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Accessing elements
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: 4

# Packing a tuple
packed_tuple = ("Alice", 25, "Engineer")

# Unpacking a tuple
(name, age, profession) = packed_tuple
print(name)       # Output: Alice
print(age)        # Output: 25
print(profession) # Output: Engineer

# Example of count()
my_tuple = (1, 2, 3, 1, 1, 4, 5)
print(my_tuple.count(1))  # Output: 3

# Example of index()
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple.index(30))  # Output: 2

my_tuple = (1, 2, 3, 4, 5, 6)
print(my_tuple[1:4])  # Output: (2, 3, 4)

