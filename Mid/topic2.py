# Topic 2: Conditions and Loops

# Part A: IQRA Grading Scale
# Part A: Grade Classifier

print("--- Part A: Three Subject Grading ---")  # duplicate print hata diya

subjects = ["Subject 1", "Subject 2", "Subject 3"]
marks = []

for sub in subjects:
    mark = float(input(f"Enter marks for {sub}: "))
    marks.append(mark)

average = sum(marks) / len(marks)

if average >= 80:
    grade = "A"
    message = "Excellent! You have mastered the material."
elif average >= 65:   
    grade = "B"
    message = "Well done! Keep pushing for higher scores."
elif average >= 50:  
    grade = "C"
    message = "Good effort, but there is room for improvement."
elif average >= 40:   
    grade = "D"
    message = "You passed, but consider reviewing the material."
else:
    grade = "F"
    message = "Don't give up! Seek help to improve your scores."

print(f"Your average is {average:.2f}. Your grade is {grade}.")
print(f"Message: {message}")
# # Part B: Even or Odd Iterator
# print("\n--- Part B: Even or Odd Iterator ---")
# n = int(input("Enter a number (N) to iterate up to: "))
# even_count = 0
# odd_count = 0
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         status = "EVEN"
#         even_count += 1
#     else:
#         status = "ODD"
#         odd_count += 1
#     print(f"{i} is {status}")
# print(f"Total even numbers: {even_count}")
# print(f"Total odd numbers: {odd_count}")

# # Part C: Number Guessing Game
# print("\n--- Part C: Number Guessing Game ---")
# target = 7
# attempts = 0
# guess = None
# while guess != target:
#     guess = int(input("Guess the number (between 1 and 10): "))
#     attempts += 1
#     if guess < target:
#         print("Too low! Try again.")
#     elif guess > target:
#         print("Too high! Try again.")
#     else:
#         print(f"Correct! You got it in {attempts} attempts.")
