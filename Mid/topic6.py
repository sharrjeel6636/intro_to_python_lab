# topic6.py – Student marks utilities

# ============================================================
# Part A: Define 4 Functions
# ============================================================

def calculate_average(marks_list):
    """Return the average of *marks_list* rounded to two decimal places.
    If the list is empty the function returns 0.0.
    """
    if not marks_list:
        return 0.0
    return round(sum(marks_list) / len(marks_list), 2)

def find_highest(marks_list):
    """Return the highest mark from *marks_list* without using max().
    If the list is empty the function returns None.
    """
    if not marks_list:
        return None
    highest = marks_list[0]
    for mark in marks_list[1:]:
        if mark > highest:
            highest = mark
    return highest

def count_passed(marks_list, pass_mark):
    """Count how many marks are greater than or equal to pass_mark.
    Returns an integer count.
    """
    count = 0
    for mark in marks_list:
        if mark >= pass_mark:
            count += 1
    return count

def format_result(name, average):
    """Return a formatted string showing the student's name, average and grade.
    The grade is derived from the average using a simple scale:
        >=80 -> A, >=65 -> B, >=50 -> C, >=40 -> D, else F.
    """
    if average >= 80:
        grade = "A"
    elif average >= 65:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"
    return f"Student: {name} | Average: {average:.2f} | Grade: {grade}"


# ============================================================
# Part B: Call All Functions
# ============================================================

if __name__ == "__main__":
    # Sample marks list as required
    marks = [72, 85, 45, 90, 63, 38, 78, 55]

    # Call calculate_average
    avg = calculate_average(marks)
    print(f"Average: {avg}")

    # Call find_highest
    highest = find_highest(marks)
    print(f"Highest mark: {highest}")

    # Call count_passed
    passed_count = count_passed(marks, pass_mark=40)
    print(f"Number passed (>=40): {passed_count}")

    # Call format_result for two different students to show grade changes
    print(format_result("Ali", avg))       
    print(format_result("Sharjeel", 90))   