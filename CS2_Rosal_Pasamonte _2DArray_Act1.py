scores = [
    [85, 90, 88],  # Student 1
    [78, 82, 80],  # Student 2
    [92, 95, 94],  # Student 3
    [70, 75, 73],  # Student 4
    [88, 85, 90]   # Student 5
]


print("Student 3 Science score:", scores[2][1])

scores[3][0] = 75
print("Updated Student 4 scores:", scores[3])

average_student1 = sum(scores[0]) / len(scores[0])
print("Average score of Student 1:", average_student1)
