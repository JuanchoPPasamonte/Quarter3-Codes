names = ["Me", "Lia", "Jake"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]  
]
daily_totals = []
num_days = len(days)
for day_index in range(num_days):
    day_sum = 0
    for person_steps in steps:
        day_sum += person_steps[day_index]
    daily_totals.append(day_sum)
max_steps = max(daily_totals)
max_day_index = daily_totals.index(max_steps)
best_day = days[max_day_index]
print("Daily Activity Analysis")
for i in range(num_days):
    print(f"{days[i]:10}: {daily_totals[i]:,}")
print(f"The most active day was {best_day} with {max_steps:,} total steps!")
