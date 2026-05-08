# Topic 4: Dictionaries and Sets

# Part A: Student Gradebook Dictionary
# Topic 4: Dictionaries and Sets

# # Part A: Student Gradebook Dictionary
# print("--- Part A: Student Gradebook ---")
# # A dictionary with 5 student names as keys and their grades as values
# gradebook = {
#     "Sharjeel": 85,
#     "Ali": 90,
#     "Raza": 78,
#     "Umar": 88,
#     "Saqib": 92
# }
# print(f"Initial gradebook: {gradebook}")
# # Print all keys, values, and items explicitly
# print(f"Keys: {list(gradebook.keys())}")
# print(f"Values: {list(gradebook.values())}")
# print(f"Items: {list(gradebook.items())}")
# # Adding a new student
# gradebook["Hamza"] = 81
# print(f"After adding Hamza: {gradebook}")
# # Updating an existing student's grade
# gradebook["Sharjeel"] = 95
# print(f"After updating Sharjeel's grade: {gradebook}")
# # Deleting a student record
# del gradebook["Raza"]
# print(f"After deleting Raza: {gradebook}")
# # Check if a specific key exists
# key_to_check = "Ali"
# print(f"Does '{key_to_check}' exist in gradebook? {key_to_check in gradebook}")
# # Using .get() for a missing student — returns None instead of raising an error
# student = "Grace"
# score = gradebook.get(student)  # No default value, so returns None if key not found
# print(f"Score for {student}: {score}")

# # Part B: Set Operations
print("\n--- Part B: Set Operations ---")
# Define the exact subject sets as required
subjects_A = {'Math', 'Python', 'Physics', 'English'}  # Set of subjects offered in curriculum A
subjects_B = {'Math', 'Chemistry', 'Python', 'Biology'}  # Set of subjects offered in curriculum B

print(f"subjects_A: {subjects_A}")
print(f"subjects_B: {subjects_B}")

# Union combines all unique elements from both sets (A ∪ B). Demonstrated using both the method and the '|' operator.
union_method = subjects_A.union(subjects_B)
union_operator = subjects_A | subjects_B
print(f"Union (method): {union_method}")
print(f"Union (operator): {union_operator}")

# Intersection finds common elements present in both sets (A ∩ B). Demonstrated using both the method and the '&' operator.
intersection_method = subjects_A.intersection(subjects_B)
intersection_operator = subjects_A & subjects_B
print(f"Intersection (method): {intersection_method}")
print(f"Intersection (operator): {intersection_operator}")

# Difference A - B yields elements in set A that are not in set B. Demonstrated using both the method and the '-' operator.
difference_AB_method = subjects_A.difference(subjects_B)
difference_AB_operator = subjects_A - subjects_B
print(f"Difference A-B (method): {difference_AB_method}")
print(f"Difference A-B (operator): {difference_AB_operator}")

# Difference B - A yields elements in set B that are not in set A. Demonstrated using both the method and the '-' operator.
difference_BA_method = subjects_B.difference(subjects_A)
difference_BA_operator = subjects_B - subjects_A
print(f"Difference B-A (method): {difference_BA_method}")
print(f"Difference B-A (operator): {difference_BA_operator}")

# Symmetric Difference gives elements that are in either set but not in both (A Δ B). Demonstrated using both the method and the '^' operator.
sym_diff_method = subjects_A.symmetric_difference(subjects_B)
sym_diff_operator = subjects_A ^ subjects_B
print(f"Symmetric Difference (method): {sym_diff_method}")
print(f"Symmetric Difference (operator): {sym_diff_operator}")