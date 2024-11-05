# Using curly braces
my_set = {1, 2, 3, 4}
my_set2 = {6,2,4,3,5,1}

# Using the set() function
#my_set = set([1, 2, 3, 4])

print(my_set)  # Output: {1, 2, 3, 4}
print(my_set2)


my_set.add(8)
print(my_set) 


my_set.update([3, 4, 5])
print(my_set)  # Output: {1, 2, 3, 4, 5, 8}

my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}


my_set = {1, 2, 3}
my_set.discard(4)  # No error even though 4 is not in the set

my_set = {1, 2, 3}
element = my_set.pop()
print(element)   # Output: 1 (or any other element)
print(my_set)    # Remaining elements after popping

my_set = {1, 2, 3}
element = my_set.pop()
print(element)   # Output: 1 (or any other element)
print(my_set)    # Remaining elements after popping


my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()



set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Output: {1, 2, 3, 4, 5}

print(set1 & set2)  # Output: {3}

print(set1 - set2)  # Output: {1, 2}

print(set1 ^ set2)  # Output: {1, 2, 4, 5}

small_set = {1, 2}
print(small_set.issubset(set1))  # Output: True



