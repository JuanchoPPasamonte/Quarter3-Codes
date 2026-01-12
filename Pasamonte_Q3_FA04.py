names = ["Me", "Lia", "Jake"]
steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]  
]

totals = [sum(person_steps) for person_steps in steps]
max_total = max(totals)
min_total = min(totals)
max_index = totals.index(max_total)
max_person = names[max_index]
difference = max_total - min_total
print("Total Steps per Person:")
for i in range(len(names)):
    print(f"- {names[i]}: {totals[i]} steps")
print(f"Person with the highest total steps: {max_person} ({max_total} steps)")
print(f"Difference between highest and lowest total: {difference} steps")
