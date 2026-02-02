scores = [
    [85, 90, 88],  # Student 1
    [78, 82, 80],  # Student 2
    [92, 95, 94],  # Student 3
    [70, 75, 73],  # Student 4
    [88, 85, 90]   # Student 5
]
print("Class Score Summary")
print(" ")
student_num = 1
for row in scores:
    total_score = sum(row)
    average_score = total_score / len(row)
    print("Student", student_num)
    print("Scores:", row)
    print("Total:", total_score)
    print("Average:", round(average_score, 2)) 
    print(" ")
    student_num = student_num + 1
