import os
import csv

# File paths
file_to_load = "PyBank/Resources/budget_data.csv"
file_to_output = "PyBank/analysis/budget_analysis.txt"

# Initialize variables
total_months = 0
net_total = 0
average_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]
previous_profit_loss = 0
monthly_changes = []

# Read the CSV file
with open(file_to_load) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader)

    # Loop through rows in the CSV
    for row in csvreader:
        # Count total months
        total_months += 1

        # Calculate net total profit/loss
        net_total += int(row[1])

        # Calculate change in profit/loss
        if total_months > 1:
            monthly_change = int(row[1]) - previous_profit_loss
            monthly_changes.append(monthly_change)

            # Check for greatest increase and decrease in profits
            if monthly_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = monthly_change

            if monthly_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = monthly_change

        # Update previous profit/loss
        previous_profit_loss = int(row[1])

# Calculate average change
if len(monthly_changes) > 0:
    average_change = sum(monthly_changes) / len(monthly_changes)

# Prepare the analysis results
analysis_results = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the analysis results
print(analysis_results)

# Write the analysis results to a text file
with open(file_to_output, "w") as txtfile:
    txtfile.write(analysis_results)