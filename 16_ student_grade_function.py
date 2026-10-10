def calculate_grade(marks):

    # Validation
    for mark in marks:
        if mark < 0 or mark > 100:
            return "Invalid Marks"

    total = 0

    for mark in marks:
        total += mark

    percentage = total / len(marks)

    if percentage >= 90:
        grade = "A"

    elif percentage >= 80:
        grade = "B"

    elif percentage >= 70:
        grade = "C"

    elif percentage >= 40:
        grade = "D"

    else:
        grade = "Fail"

    return total, percentage, grade


marks = []

for i in range(5):
    mark = int(input(f"Enter mark for subject {i+1}: "))
    marks.append(mark)

result = calculate_grade(marks)

if result == "Invalid Marks":

    print("Invalid Marks Entered")

else:

    total, percentage, grade = result

    print("Total Marks =", total)
    print("Percentage =", percentage)
    print("Grade =", grade)