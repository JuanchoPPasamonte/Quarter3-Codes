scores = [
    [85, 90, 88],  # Student 1
    [78, 82, 80],  # Student 2
    [92, 95, 94],  # Student 3
    [75, 75, 73],  # Student 4
    [88, 85, 90]   # Student 5
]

print("Student Scores Summary:\n")

for i in range(len(scores)):
    total = sum(scores[i])
    average = total / len(scores[i])
    print("Student", i + 1, "scores:", scores[i])
    print("  Total:", total)
    print("  Average:", average)
    print()

max_score = scores[0][0]
min_score = scores[0][0]

for row in scores:
    for value in row:
        if value > max_score:
            max_score = value
        if value < min_score:
            min_score = value

print("Highest score in the dataset:", max_score)
print("Lowest score in the dataset:", min_score)
