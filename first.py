# Basic Python Variables - Learning Guide

# 1. String Variables
name = input("Enter your name: ")
print(f"Hello, {name}!")
print(f"Type: {type(name)}")

# 2. Integer Variables
age = int(input("Enter your age: "))
print(f"You are {age} years old")
print(f"Type: {type(age)}")

# 3. Float Variables
height = float(input("Enter your height in meters: "))
print(f"Your height is {height}m")
print(f"Type: {type(height)}")

# 4. Boolean Variables
is_student = input("Are you a student? (yes/no): ").lower() == "yes"
print(f"Student status: {is_student}")
print(f"Type: {type(is_student)}")

# 5. List (multiple values)
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")
print(f"Type: {type(numbers)}")

# 6. Dictionary (key-value pairs)
person = {"name": name, "age": age, "height": height}
print(f"Person info: {person}")
print(f"Type: {type(person)}")

# 7. Tuple (immutable list)
coordinates = (10, 20)
print(f"Coordinates: {coordinates}")
print(f"Type: {type(coordinates)}")

# 8. Set (unique values)
colors = {"red", "blue", "green"}
print(f"Colors: {colors}")
print(f"Type: {type(colors)}")