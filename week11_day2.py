# ----------------------------------------
# Day 2 Review Activity: My Personal Info Generator
# ----------------------------------------

print(" Welcome to the Python Review Activity!")
print("You’ll review variables, strings, numbers, and print formatting.\n")

# Step 1: Create Variables
# TODO: Replace the values below with your own info
first_name = "Benji"
age = 16
favorite_color = "Blue"
favorite_number = 3

# Step 2: Practice String Operations
# 1. Print your name in uppercase
print(first_name.upper())

# 2. Print how many letters are in your name
print(len(first_name))

# 3. Combine your name and favorite color into one message
print("My name is " + first_name + " and my favorite color is " + favorite_color + ".")

# Step 3: Math Practice
# Use arithmetic operators with your favorite number
print("My favorite number doubled is:", favorite_number * 2)
print("My favorite number squared is:", favorite_number ** 2)
print("My favorite number plus my age is:", favorite_number + age)

# Step 4: User Input Practice
# Ask the user two questions and combine answers
hobby = input("What’s your favorite hobby? ")
pet_name = input("What’s your pet’s name? ")
print("Cool! So you like", hobby, "and your pet’s name is", pet_name + "!")

# ⚙️ Step 5: Final Challenge (combine it all)
# Use math and strings together
future_age = age + 5
print(f"In 5 years, {first_name} will be {future_age} years old and still love the color {favorite_color}!")
