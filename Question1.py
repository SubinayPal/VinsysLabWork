age = int(input("Enter your age : "))

if age >= 18:
    print("You are eligible to vote.")
elif age >= 13 and age <= 17:
    print("You're a teenager.")
else:
    print("You're a child.")