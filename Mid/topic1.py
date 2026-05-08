# Topic 1: Variables, Input & Operators

# # Part A: Capture user data and display with types
# print("--- Part A: User Data Collection ---")
# name = input("Enter your Name: ")
# age = int(input("Enter your Age: "))
# cgpa = float(input("Enter your CGPA: "))
# # Note: int('42.75') raises ValueError because int() cannot parse a string containing a decimal point directly.

# is_student = input("Are you a student? (yes/no): ").lower() == 'yes'

# print(f"Hello {name}! You are {age} years old. Your CGPA is {cgpa}. Student: {is_student}")
# print(f"Name type: {type(name)}")
# print(f"Age type: {type(age)}")
# print(f"CGPA type: {type(cgpa)}")
# print(f"Student type: {type(is_student)}")

 # Part B: Calculator with arithmetic operations
# print("\n--- Part B: Basic Calculator ---")
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# print(f"Addition: {num1} + {num2} = {num1 + num2}")
# print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
# print(f"Multiplication: {num1} * {num2} = {num1 * num2}")

# # Safety: Prevent division by zero
# if num2 != 0:
#     print(f"Division: {num1} / {num2} = {num1 / num2}")
#     print(f"Floor Division: {num1} // {num2} = {num1 // num2}")
#     print(f"Modulus: {num1} % {num2} = {num1 % num2}")
# else:
#     print("Cannot divide by zero!")

# print(f"Exponentiation: {num1} ** {num2} = {num1 ** num2}")


# Part C: String to Float Conversion

print("\n--- Part C: String to Float Conversion ---")  # comment hata diya


num_str = input("Enter a number (e.g., 42.75): ")

num_float = float(num_str)
result = num_float * 2
print(f"Result after converting to float and multiplying by 2: {result}")

print("\n--- Demonstrating int conversion error ---")
try:
    int_val = int('42.75')
    print(f"Converted value: {int_val}")
except ValueError as e:
    print(f"Error converting '42.75' to int: {e}")

