# topic5.py – String method practice

# Part A – Demonstrate common string methods

sentence = "  Hello, Welcome to Python Programming!  "

print("Original:", repr(sentence))
print("strip():", sentence.strip())
print("lower():", sentence.lower())
print("upper():", sentence.upper())
print("title():", sentence.title())
print("replace('Python', 'Advanced Python'):", sentence.replace('Python', 'Advanced Python'))
print("split(','):", sentence.split(','))
print("find('Welcome'):", sentence.find('Welcome'))
print("count('o'):", sentence.count('o'))

stripped = sentence.strip()
print("startswith('Hello'):", stripped.startswith('Hello'))
print("endswith('!'):", stripped.endswith('!'))

# Part B – Specific slicing operations on the word 'PROGRAMMING'
# word = 'PROGRAMMING'
# print('First character:', word[0])
# print('Last character:', word[-1])
# print('Slice from index 3 to 7 (inclusive of 3, exclusive of 7):', word[3:7])
# print('Every other character (step 2):', word[::2])
# print('Reversed word:', word[::-1])

# # Part C – Price input, discount, and formatted display
# price_input = input('Enter the original price: ')
# try:
#     price = float(price_input)
#     discounted = price * 0.9  # Apply a 10% discount
#     print(f'Discounted price: ${discounted:.2f}')
# except ValueError:
#     print('Invalid price entered. Please provide a numeric value.')
