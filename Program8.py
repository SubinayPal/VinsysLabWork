# Example of a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(person)

# Accessing values
print(person["name"])  # Output: Alice
print(person["age"])   # Output: 30

print(person.get("city"))       # Output: New York
print(person.get("country"))    # Output: None (key does not exist)

# Adding a new item
person["country"] = "USA"
print(person)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}

# Updating an existing item
person["age"] = 31
print(person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'}


del person["city"]
print(person)  # Output: {'name': 'Alice', 'age': 31, 'country': 'USA'}

age = person.pop("age")
print(age)     # Output: 31
print(person)  # Output: {'name': 'Alice', 'country': 'USA'}

last_item = person.popitem()
print(last_item)  # Output: ('country', 'USA')
print(person)     # Output: {'name': 'Alice'}



# Loop through keys
for key in person:
    print(key)

# Loop through values
for value in person.values():
    print(value)

# Loop through key-value pairs
for key, value in person.items():
    print(key, ":", value)


person = {"name": "Alice", "age": 30}
person.update({"city": "New York", "country": "USA"})
print(person)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}

person.clear()
print(person)  # Output: {}




