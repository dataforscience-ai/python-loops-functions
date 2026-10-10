marks=[]
n=int(input("How many students? "))
for i in range(n):
    mark=int(input("Enter marks for student {}: ".format(i + 1)))
    marks.append(mark)
highest_mark = marks[0] if n > 0 else 0
lowest_mark = marks[0] if n > 0 else 0
total_marks = 0
total_count = 0
pass_count = 0
fail_count = 0
for mark in marks:
    total_marks += mark
    total_count += 1
    if mark > highest_mark:
        highest_mark = mark
    if mark < lowest_mark:
        lowest_mark = mark
    if mark >= 40:
        pass_count += 1
    else:
        fail_count += 1
average_mark = total_marks / total_count if total_count > 0 else 0
print("Highest mark:", highest_mark)    
print("Lowest mark:", lowest_mark)
print("Average mark:", average_mark)
print("Number of students who passed:", pass_count)
print("Number of students who failed:", fail_count) 