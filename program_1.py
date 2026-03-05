# By Nathan Nelsen
# Written 3/5/26
# Rainfall

# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year,
# the average monthly rainfall, # and the months with the highest and lowest amounts.

rainfall = []

for month in range(1, 13):
    amount = float(input(f"Enter total rainfall for month {month}: "))
    rainfall.append(amount)

total_rainfall = sum(rainfall)
average_rainfall = total_rainfall / 12
highest_rainfall = max(rainfall)
lowest_rainfall = min(rainfall)

highest_month = rainfall.index(highest_rainfall) + 1
lowest_month = rainfall.index(lowest_rainfall) + 1

print("Total rainfall for the year:", total_rainfall)
print("Average monthly rainfall:", format(average_rainfall, '.2f'))
print("Month with the highest amount of rainfall:", highest_month, "Amount of rainfall:", highest_rainfall)
print("Month with the lowest amount of rainfall:", lowest_month, "Amount of rainfall:", lowest_rainfall)
