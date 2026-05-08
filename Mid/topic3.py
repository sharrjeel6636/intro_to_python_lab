# Topic 3: Lists and Tuples

# Part A: Student Marks List
print("--- Part A: Student Marks List ---")
# 1. Original list
marks = [75, 45, 90, 60, 35, 82]
print(f"1. Original list: {marks}")

# 2. First and last elements
print(f"2. First element (marks[0]): {marks[0]}")
print(f"   Last element (marks[-1]): {marks[-1]}")

# 3. Slice marks[1:4]
print(f"3. Slice marks[1:4]: {marks[1:4]}")

# 4. Append 88
marks.append(88)
print(f"4. After appending 88: {marks}")

# 5. Insert 95 at index 2
marks.insert(2, 95)
print(f"5. After inserting 95 at index 2: {marks}")

# 6. Remove the lowest mark
lowest = min(marks)
marks.remove(lowest)
print(f"6. After removing the lowest mark ({lowest}): {marks}")

# 7. Sort ascending
marks.sort()
print(f"7. After sorting ascending: {marks}")

# 8. Sort descending (reverse)
marks.sort(reverse=True)
print(f"8. After sorting descending: {marks}")

# 9. Index of 95
index_95 = marks.index(95)
print(f"9. Index of 95: {index_95}")

# 10. Length of the list
print(f"10. Length of list: {len(marks)}")

 # Part B: Tuple Immutability
print("\n--- Part B: Tuple Immutability ---")
student = ('Ali Ahmed', 20, 'Computer Science', 3.75)
print(f"Student name: {student[0]}")
print(f"Program: {student[2]}")
try:
    # Attempt to modify the tuple (should raise TypeError)
    student[0] = 'New Name'
except TypeError as e:
    print(f"Error captured when trying to modify tuple: {e}")

# # Part C: List Comprehensions
print("\n--- Part C: List Comprehensions ---")
marks = [75, 45, 90, 60, 35, 82]
# Marks >= 60
passed_marks = [m for m in marks if m >= 60]
print(f"Marks >= 60: {passed_marks}")
# Square of all marks
squared_marks = [m**2 for m in marks]
print(f"Squares of all marks: {squared_marks}")
