# ============================================================
# PYTHON BASICS — Complete Syntax Reference for Developers
# Ravi Goswami | python-mastery-2026
# Run this file: python3 python_basics.py
# ============================================================


# ============================================================
# 1. PRINT — your console.log()
# ============================================================

print("Hello, Ravi!")                        # simple string
print("Name:", "Ravi", "Age:", 25)           # multiple values, auto space
print("Line 1\nLine 2")                      # \n for new line
print("-" * 40)                              # repeat string 40 times (useful for dividers)
print()                                      # empty print = blank line


# ============================================================
# 2. VARIABLES & DATA TYPES
# ============================================================

# No let/const/var — just assign directly
name = "Ravi"                   # str
age = 25                        # int
salary = 2500000.50             # float
is_senior = True                # bool — Capital T/F (not lowercase like JS)
nothing = None                  # None — Python's null/undefined

# Check type of any variable
print(type(name))               # <class 'str'>
print(type(age))                # <class 'int'>
print(type(is_senior))          # <class 'bool'>
print(type(nothing))            # <class 'NoneType'>

# Multiple assignment in one line
x, y, z = 10, 20, 30
print(x, y, z)                  # 10 20 30

# Swap variables (Python magic — no temp variable needed)
x, y = y, x
print(x, y)                     # 20 10


# ============================================================
# 3. STRINGS — Most Important Data Type
# ============================================================

first = "Ravi"
last = "Goswami"

# Concatenation
full_name = first + " " + last
print(full_name)                # Ravi Goswami

# f-strings — USE THESE ALWAYS (like JS template literals)
print(f"Hello, {first} {last}!")
print(f"2 + 2 = {2 + 2}")                   # can put expressions inside {}
print(f"Salary: {salary:,.2f}")             # format numbers: 2,500,000.50

# String methods
sentence = "  hello world  "
print(sentence.strip())                     # remove whitespace: "hello world"
print(sentence.strip().upper())             # "HELLO WORLD"
print(sentence.strip().capitalize())        # "Hello world"
print("hello".replace("hello", "hi"))       # "hi"
print("Ravi Goswami".split(" "))            # ['Ravi', 'Goswami']
print(",".join(["a", "b", "c"]))            # "a,b,c"
print("hello world".find("world"))          # 6 (index position)
print("hello".startswith("he"))             # True
print("hello".endswith("lo"))               # True
print(len("Ravi"))                          # 4

# String slicing — like JS substring but cleaner
text = "Hello World"
print(text[0])                              # H (first char)
print(text[-1])                             # d (last char)
print(text[0:5])                            # Hello (index 0 to 4)
print(text[6:])                             # World (index 6 to end)
print(text[:5])                             # Hello (start to index 4)
print(text[::-1])                           # dlroW olleH (reverse!)

# Multi-line strings
message = """
This is a
multi-line string
in Python
"""
print(message)

# Check if substring exists
print("world" in "hello world")             # True
print("world" not in "hello world")         # False


# ============================================================
# 4. NUMBERS & MATH
# ============================================================

a, b = 10, 3

print(a + b)        # 13  — addition
print(a - b)        # 7   — subtraction
print(a * b)        # 30  — multiplication
print(a / b)        # 3.333... — division (always returns float)
print(a // b)       # 3   — floor division (like Math.floor)
print(a % b)        # 1   — modulo (remainder)
print(a ** b)       # 1000 — exponent (10 to the power 3)

# Math shortcuts
count = 0
count += 1          # same as count = count + 1
count -= 1
count *= 2

# Built-in math functions
print(abs(-42))         # 42
print(round(3.14159, 2))  # 3.14
print(max(1, 5, 3))     # 5
print(min(1, 5, 3))     # 1
print(sum([1, 2, 3]))   # 6
print(pow(2, 8))        # 256

# Import math module for advanced operations
import math
print(math.sqrt(144))       # 12.0
print(math.pi)              # 3.14159...
print(math.ceil(4.1))       # 5
print(math.floor(4.9))      # 4


# ============================================================
# 5. INPUT — Getting User Input
# ============================================================

# input() always returns a STRING
# Uncomment these lines to try interactive input:

# user_name = input("Enter your name: ")
# user_age = input("Enter your age: ")        # this is a string!
# user_age_int = int(input("Enter your age: "))  # convert to int

# For this script we'll simulate input with variables:
user_name = "Ravi"
user_age = "25"                             # as if from input()

# Always convert types when needed
age_as_int = int(user_age)                  # str → int
age_as_float = float(user_age)              # str → float
back_to_str = str(age_as_int)               # int → str
is_true = bool(1)                           # 1 → True, 0 → False

print(f"Name: {user_name}, Age: {age_as_int}, Type: {type(age_as_int)}")


# ============================================================
# 6. IF / ELIF / ELSE — Conditionals
# ============================================================

experience = 6

# Basic if/elif/else
if experience >= 8:
    print("Staff Engineer level")
elif experience >= 5:
    print("Senior Engineer level")          # This prints
elif experience >= 2:
    print("Mid-level Engineer")
else:
    print("Junior Engineer")

# Comparison operators
print(5 == 5)       # True  — equality
print(5 != 3)       # True  — not equal
print(5 > 3)        # True  — greater than
print(5 < 3)        # False — less than
print(5 >= 5)       # True  — greater than or equal
print(5 <= 4)       # False — less than or equal

# Logical operators (and/or/not — NOT &&/||/!)
salary = 2500000
city = "Noida"

if salary > 2000000 and city == "Noida":
    print("High earner in Noida!")

if salary < 1000000 or experience > 5:
    print("Either low salary or high experience")

if not is_senior:
    print("Not a senior")
else:
    print("Is a senior!")

# One-liner if (ternary — like JS condition ? a : b)
level = "Senior" if experience >= 5 else "Junior"
print(f"Level: {level}")

# Checking None
value = None
if value is None:                           # use 'is None' not '== None'
    print("Value is None")

if value is not None:
    print("Has a value")

# Truthy / Falsy (same concept as JS)
# Falsy in Python: None, 0, "", [], {}, set()
# Everything else is truthy

if "":
    print("won't print — empty string is falsy")

if "Ravi":
    print("prints — non-empty string is truthy")

if []:
    print("won't print — empty list is falsy")

if [1, 2, 3]:
    print("prints — non-empty list is truthy")


# ============================================================
# 7. LISTS — Python's Arrays
# ============================================================

# Create a list
skills = ["Node.js", "Python", "NestJS", "Docker", "Kubernetes"]

# Access elements
print(skills[0])            # Node.js (first)
print(skills[-1])           # Kubernetes (last)
print(skills[1:3])          # ['Python', 'NestJS'] (slicing)

# Add elements
skills.append("FastAPI")            # add to end
skills.insert(1, "TypeScript")      # insert at index 1
print(skills)

# Remove elements
skills.remove("Docker")             # remove by value
popped = skills.pop()               # remove and return last item
popped_at = skills.pop(0)           # remove and return at index
print(f"Removed: {popped}, {popped_at}")
print(skills)

# Check membership
print("Python" in skills)           # True
print("Java" in skills)             # False

# List info
print(len(skills))                  # number of items
print(skills.count("Python"))       # how many times "Python" appears
print(skills.index("NestJS"))       # index of "NestJS" (first occurrence)

# Get first and last index
print(skills[0])                    # first element: "Node.js"
print(skills[-1])                   # last element: "Kubernetes"

# Find index of first occurrence
first_index = skills.index("Python")        # returns first occurrence index
print(f"First 'Python' at index: {first_index}")

# Find index of last occurrence (no built-in method, use trick)
last_index = len(skills) - 1 - skills[::-1].index("Python")  # reverse slice trick
print(f"Last 'Python' at index: {last_index}")

# Sort
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()                      # sorts in place (modifies original)
print(numbers)                      # [1, 1, 2, 3, 4, 5, 6, 9]

numbers.sort(reverse=True)          # descending
print(numbers)

sorted_copy = sorted(numbers)       # returns NEW sorted list (original unchanged)

# List operations
list_a = [1, 2, 3]
list_b = [4, 5, 6]
combined = list_a + list_b          # [1, 2, 3, 4, 5, 6]
repeated = list_a * 3               # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Useful list functions
print(min(numbers))                 # smallest
print(max(numbers))                 # largest
print(sum(numbers))                 # total

# Copy a list (important — assignment doesn't copy!)
original = [1, 2, 3]
wrong_copy = original               # NOT a copy — both point to same list!
right_copy = original.copy()        # actual copy
right_copy2 = original[:]          # also a copy (slice trick)

wrong_copy.append(4)
print(original)                     # [1, 2, 3, 4] — original changed! ❌
print(right_copy)                   # [1, 2, 3] — safe ✓


# ============================================================
# 8. TUPLES — Immutable Lists (read-only)
# ============================================================

# Use tuples when data should NOT change
coordinates = (28.6139, 77.2090)    # Delhi coordinates
rgb_color = (255, 128, 0)

print(coordinates[0])               # 28.6139
# coordinates[0] = 0               # ERROR — tuples are immutable

# Unpack a tuple
lat, lng = coordinates
print(f"Lat: {lat}, Lng: {lng}")

# Single item tuple needs trailing comma
single = (42,)                      # NOT (42) — that's just an int in parens


# ============================================================
# 9. SETS — Unique Values Only
# ============================================================

# Sets automatically remove duplicates
tags = {"python", "backend", "python", "api", "backend"}
print(tags)                         # {'python', 'backend', 'api'} — no duplicates!

# Add / Remove
tags.add("fastapi")
tags.discard("api")                 # remove if exists (no error if not found)
print(tags)

# Set operations — great for comparisons
backend_skills = {"python", "nodejs", "sql", "docker"}
ai_skills = {"python", "pytorch", "numpy", "sql"}

print(backend_skills & ai_skills)   # intersection: {'python', 'sql'}
print(backend_skills | ai_skills)   # union: all unique items
print(backend_skills - ai_skills)   # difference: in backend but not ai

# Check membership (faster than lists for large data)
print("python" in backend_skills)   # True


# ============================================================
# 10. DICTIONARIES — Python's Objects/HashMaps
# ============================================================

# Create a dictionary (like JS objects)
engineer = {
    "name": "Ravi Goswami",
    "age": 25,
    "role": "Senior Software Engineer",
    "skills": ["Node.js", "Python", "NestJS"],
    "is_senior": True,
    "salary": 2500000,
    "address": {                    # nested dictionary
        "city": "Noida",
        "state": "UP",
        "country": "India"
    }
}

# Access values
print(engineer["name"])             # Ravi Goswami
print(engineer["address"]["city"])  # Noida (nested access)

# Safe access with .get() — returns None if key doesn't exist (no KeyError)
print(engineer.get("phone"))        # None — no error!
print(engineer.get("phone", "N/A")) # N/A — provide default value

# Add / Update
engineer["email"] = "ravi@example.com"     # add new key
engineer["age"] = 26                        # update existing key
print(engineer["age"])              # 26

# Delete
del engineer["age"]                 # delete a key
removed = engineer.pop("salary")    # delete and return value
print(f"Removed salary: {removed}")

# Check if key exists
print("name" in engineer)           # True
print("phone" in engineer)          # False

# Get all keys, values, items
print(engineer.keys())              # dict_keys([...])
print(engineer.values())            # dict_values([...])
print(engineer.items())             # dict_items([(key, val), ...])

# Update multiple keys at once (like Object.assign in JS)
engineer.update({"role": "Tech Lead", "team_size": 14})
print(engineer["role"])             # Tech Lead

# Merge two dicts (Python 3.9+)
extra_info = {"github": "ravigoswami25", "linkedin": "goswamiravi"}
full_profile = engineer | extra_info    # merge — like JS spread {...obj1, ...obj2}
# OR
full_profile = {**engineer, **extra_info}  # older style spread (works on all versions)


# ============================================================
# 11. FOR LOOPS
# ============================================================

skills = ["Python", "Node.js", "FastAPI", "Docker"]

# Basic for loop (like JS for...of)
for skill in skills:
    print(f"Skill: {skill}")

# With index — use enumerate() always (never range(len(list)))
for index, skill in enumerate(skills):
    print(f"{index}: {skill}")

# Start enumerate from 1
for index, skill in enumerate(skills, start=1):
    print(f"{index}. {skill}")

# Loop over a range
for i in range(5):
    print(i)                        # 0, 1, 2, 3, 4

for i in range(1, 6):
    print(i)                        # 1, 2, 3, 4, 5

for i in range(0, 10, 2):
    print(i)                        # 0, 2, 4, 6, 8 (step by 2)

for i in range(10, 0, -1):
    print(i)                        # 10, 9, 8... 1 (countdown)

# Loop over dictionary
for key in engineer:
    print(key)                      # prints keys

for key, value in engineer.items():
    print(f"{key}: {value}")        # prints key-value pairs

# Loop over string
for char in "Ravi":
    print(char)                     # R, a, v, i

# Zip — loop over two lists together (like JS zip)
names = ["Ravi", "Amit", "Priya"]
scores = [95, 87, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# break — exit loop early
for i in range(10):
    if i == 5:
        break
    print(i)                        # 0, 1, 2, 3, 4

# continue — skip current iteration
for i in range(10):
    if i % 2 == 0:
        continue                    # skip even numbers
    print(i)                        # 1, 3, 5, 7, 9

# for...else — runs if loop completed without break
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed without break")  # this prints


# ============================================================
# 12. WHILE LOOPS
# ============================================================

count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1                      # ALWAYS increment or you get infinite loop!

# While with break
attempts = 0
while True:                         # infinite loop — use carefully
    attempts += 1
    if attempts >= 3:
        print("Max attempts reached")
        break

# Simulating a do-while (Python has no do-while)
number = 0
while True:
    number += 1
    print(number)
    if number >= 3:
        break


# ============================================================
# 13. LIST COMPREHENSIONS — Python's Superpower
# ============================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Basic: [expression for item in iterable]
squares = [n ** 2 for n in numbers]
print(squares)                      # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# With condition: [expression for item in iterable if condition]
evens = [n for n in numbers if n % 2 == 0]
print(evens)                        # [2, 4, 6, 8, 10]

# Transform strings
skills = ["  python  ", "  nodejs  ", "  fastapi  "]
clean = [s.strip().title() for s in skills]
print(clean)                        # ['Python', 'Nodejs', 'Fastapi']

# Equivalent to:
# clean = []
# for s in skills:
#     clean.append(s.strip().title())

# Dict comprehension
salaries = {"Ravi": 2500000, "Amit": 1800000, "Priya": 3200000}
in_lakhs = {name: sal / 100000 for name, sal in salaries.items()}
print(in_lakhs)                     # {'Ravi': 25.0, 'Amit': 18.0, 'Priya': 32.0}

# Set comprehension
unique_lengths = {len(skill) for skill in ["Python", "Go", "Rust", "Python"]}
print(unique_lengths)               # {2, 4, 6} — unique lengths, no duplicates


# ============================================================
# 14. JSON — Parsing & Creating (Critical for APIs)
# ============================================================

import json

# ── JSON String → Python Dict (parsing)
json_string = '{"name": "Ravi", "age": 25, "skills": ["Python", "Node.js"]}'

data = json.loads(json_string)          # loads = load from String
print(type(data))                       # <class 'dict'>
print(data["name"])                     # Ravi
print(data["skills"][0])               # Python

# ── Python Dict → JSON String (serializing)
profile = {
    "name": "Ravi Goswami",
    "role": "Senior Engineer",
    "skills": ["Python", "Node.js"],
    "active": True,
    "salary": None                      # None becomes null in JSON
}

json_output = json.dumps(profile)               # dumps = dump to String
print(json_output)

json_pretty = json.dumps(profile, indent=2)     # pretty print with indentation
print(json_pretty)

# ── Read JSON from a file
# with open("data.json", "r") as f:
#     file_data = json.load(f)          # load (no 's') = from file

# ── Write JSON to a file
# with open("output.json", "w") as f:
#     json.dump(profile, f, indent=2)   # dump (no 's') = to file

# ── Nested JSON parsing
api_response = """
{
    "status": "success",
    "data": {
        "user": {
            "id": 101,
            "name": "Ravi",
            "address": {
                "city": "Noida",
                "country": "India"
            }
        },
        "projects": [
            {"id": 1, "name": "Resume CLI", "status": "done"},
            {"id": 2, "name": "Job Market API", "status": "in_progress"}
        ]
    }
}
"""

parsed = json.loads(api_response)

# Navigate nested structure
print(parsed["data"]["user"]["name"])               # Ravi
print(parsed["data"]["user"]["address"]["city"])    # Noida
print(parsed["data"]["projects"][0]["name"])        # Resume CLI

# Loop through nested list
for project in parsed["data"]["projects"]:
    print(f"Project: {project['name']} — {project['status']}")

# Safe nested access using .get()
city = parsed.get("data", {}).get("user", {}).get("address", {}).get("city", "Unknown")
print(f"City: {city}")              # Noida


# ============================================================
# 15. ERROR HANDLING — try/except
# ============================================================

# Basic try/except (like JS try/catch)
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Catch specific errors
try:
    number = int("not-a-number")
except ValueError as e:
    print(f"ValueError: {e}")

# Catch multiple errors
try:
    data = {"name": "Ravi"}
    print(data["age"])              # KeyError — key doesn't exist
except KeyError as e:
    print(f"Key not found: {e}")
except TypeError as e:
    print(f"Type error: {e}")

# Catch any exception
try:
    risky_code = 1 / 0
except Exception as e:
    print(f"Something went wrong: {e}")
    print(f"Error type: {type(e).__name__}")

# finally — always runs (like JS finally)
try:
    file_opened = True
    result = 10 / 2
except ZeroDivisionError:
    print("Division error")
finally:
    print("This always runs — use for cleanup")

# else — runs only if NO exception occurred
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error!")
else:
    print(f"Success! Result: {result}")     # this prints


# ============================================================
# 16. FILE HANDLING
# ============================================================

# Write to a file
with open("test_output.txt", "w") as f:     # 'w' = write (overwrites)
    f.write("Hello from Python!\n")
    f.write("Second line\n")

# Append to a file
with open("test_output.txt", "a") as f:     # 'a' = append
    f.write("Third line\n")

# Read entire file
with open("test_output.txt", "r") as f:     # 'r' = read
    content = f.read()
    print(content)

# Read line by line (memory efficient for large files)
with open("test_output.txt", "r") as f:
    for line in f:
        print(line.strip())                 # strip() removes the \n

# Read all lines into a list
with open("test_output.txt", "r") as f:
    lines = f.readlines()                   # ['Hello...\n', 'Second...\n']
    print(lines)

# Write JSON to file (combining skills!)
import json
data = {"name": "Ravi", "skills": ["Python", "FastAPI"]}
with open("profile.json", "w") as f:
    json.dump(data, f, indent=2)
print("JSON file written!")

# Read JSON from file
with open("profile.json", "r") as f:
    loaded = json.load(f)
print(loaded["name"])               # Ravi


# ============================================================
# 17. STRING FORMATTING — Advanced
# ============================================================

name = "Ravi"
salary = 2500000
pi = 3.14159265

# f-string formatting
print(f"{'Name':<15} {'Salary':>12}")       # align left/right
print(f"{name:<15} {salary:>12,}")          # left-align name, right-align with commas

# Number formatting
print(f"{pi:.2f}")                          # 3.14 (2 decimal places)
print(f"{pi:.4f}")                          # 3.1416
print(f"{salary:,}")                        # 2,500,000 (thousands separator)
print(f"{0.256:.1%}")                       # 25.6% (percentage)
print(f"{255:08b}")                         # 11111111 (binary, padded to 8 chars)
print(f"{255:x}")                           # ff (hexadecimal)


# ============================================================
# 18. USEFUL BUILT-IN FUNCTIONS
# ============================================================

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

print(len(numbers))                 # 11 — length
print(sum(numbers))                 # total
print(min(numbers))                 # 1
print(max(numbers))                 # 9
print(sorted(numbers))              # sorted copy (ascending)
print(sorted(numbers, reverse=True))# sorted copy (descending)
print(list(reversed(numbers)))      # reversed copy
print(list(set(numbers)))           # remove duplicates

# all() and any() — super useful
scores = [85, 90, 78, 92, 88]
print(all(s >= 70 for s in scores)) # True — all above 70?
print(any(s >= 90 for s in scores)) # True — any above 90?

# map() — apply function to every item
doubled = list(map(lambda x: x * 2, [1, 2, 3, 4]))
print(doubled)                      # [2, 4, 6, 8]

# filter() — keep items that match condition
big_scores = list(filter(lambda s: s >= 88, scores))
print(big_scores)                   # [90, 92, 88]

# zip() — pair up two lists
names = ["Ravi", "Amit", "Priya"]
roles = ["Tech Lead", "SDE", "SDE2"]
pairs = list(zip(names, roles))
print(pairs)                        # [('Ravi', 'Tech Lead'), ...]

# Convert zip to dict
role_map = dict(zip(names, roles))
print(role_map)                     # {'Ravi': 'Tech Lead', ...}

# enumerate() — index + value
for i, name in enumerate(names, 1):
    print(f"{i}. {name}")


# ============================================================
# 19. REAL WORLD EXAMPLE — Putting It All Together
# ============================================================

print("\n" + "=" * 50)
print("REAL WORLD: Engineer Profile Analyzer")
print("=" * 50)

# Sample data (like an API response)
engineers_json = """
[
    {"name": "Ravi", "role": "Tech Lead", "exp": 6, "salary": 2500000, "skills": ["Python", "Node.js", "NestJS"]},
    {"name": "Amit", "role": "SDE", "exp": 3, "salary": 1200000, "skills": ["React", "Node.js"]},
    {"name": "Priya", "role": "SDE2", "exp": 5, "salary": 2000000, "skills": ["Python", "Django", "AWS"]},
    {"name": "Rahul", "role": "SDE", "exp": 2, "salary": 900000, "skills": ["Java", "Spring"]},
    {"name": "Sneha", "role": "SDE2", "exp": 4, "salary": 1800000, "skills": ["Python", "FastAPI", "PostgreSQL"]}
]
"""

# Parse JSON
engineers = json.loads(engineers_json)

# Filter: engineers who know Python
python_engineers = [e for e in engineers if "Python" in e["skills"]]
print(f"\nPython engineers: {[e['name'] for e in python_engineers]}")

# Average salary
avg_salary = sum(e["salary"] for e in engineers) / len(engineers)
print(f"Average salary: ₹{avg_salary:,.0f}")

# Highest paid
top_earner = max(engineers, key=lambda e: e["salary"])
print(f"Top earner: {top_earner['name']} — ₹{top_earner['salary']:,}")

# Sort by experience
by_exp = sorted(engineers, key=lambda e: e["exp"], reverse=True)
print("\nBy experience (most first):")
for e in by_exp:
    print(f"  {e['name']:<10} {e['exp']} years  ₹{e['salary']:>10,}")

# Group by role
from collections import defaultdict
by_role = defaultdict(list)
for e in engineers:
    by_role[e["role"]].append(e["name"])

print("\nBy role:")
for role, names in by_role.items():
    print(f"  {role}: {', '.join(names)}")

# Build a summary dict
summary = {
    "total_engineers": len(engineers),
    "avg_salary_lpa": round(avg_salary / 100000, 1),
    "top_earner": top_earner["name"],
    "python_count": len(python_engineers)
}

print("\nSummary:")
print(json.dumps(summary, indent=2))


# ============================================================
# QUICK REFERENCE CHEAT SHEET
# ============================================================
"""
VARIABLES:     x = 5  |  name = "Ravi"  |  is_ok = True  |  val = None
PRINT:         print(f"Hello {name}")
INPUT:         name = input("Enter: ")  — always returns str, convert if needed
TYPES:         int("5") | float("3.14") | str(42) | bool(1)

IF:            if x > 5:  |  elif x == 5:  |  else:
TERNARY:       result = "yes" if x > 5 else "no"

FOR:           for item in list:  |  for i in range(5):  |  for i, v in enumerate(list):
WHILE:         while condition:   |  break  |  continue

LIST:          [1,2,3]  |  list.append()  |  list.pop()  |  list[0]  |  list[-1]  |  list[1:3]
TUPLE:         (1,2,3)  — immutable
SET:           {1,2,3}  — unique values
DICT:          {"key": "val"}  |  d["key"]  |  d.get("key", default)  |  d.items()

LIST COMP:     [x*2 for x in list if x > 0]
DICT COMP:     {k: v*2 for k, v in dict.items()}

JSON PARSE:    json.loads(string)  →  dict
JSON MAKE:     json.dumps(dict, indent=2)  →  string
JSON READ:     json.load(file)  →  dict
JSON WRITE:    json.dump(dict, file, indent=2)

TRY:           try:  |  except ValueError as e:  |  finally:  |  else:
FILE:          with open("f.txt", "r") as f:  — modes: r, w, a

STRING:        f"Hello {name}"  |  .strip()  |  .upper()  |  .split()  |  .join()  |  "x" in s
MATH:          + - * /  |  // (floor div)  |  % (modulo)  |  ** (power)
"""

print("\n✅ All done! You now know Python basics. Push this to GitHub!")