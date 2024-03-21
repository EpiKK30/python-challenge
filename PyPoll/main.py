# Dependencies
import os
import csv

# File paths to load and output
file_to_load = "PyPoll/Resources/election_data.csv"
file_to_output = "PyPoll/analysis/election_analysis.txt"

# Initialize variables and track various parameters
total_votes = 0
candidates = []
candidate_votes = {}

# Read the CSV file
with open(file_to_load) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header row
    next(csvreader)

    # Loop through rows in the CSV
    for row in csvreader:
        # Count total votes
        total_votes += 1

        # Collect candidates and their votes
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1

# Analyze the data and determine the winner
winner = ""
winning_votes = 0
analysis_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    analysis_results += f"{candidate}: {percentage:.3f}% ({votes})\n"
    if votes > winning_votes:
        winning_votes = votes
        winner = candidate

# Generate final analysis results
analysis_results += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

# Print analysis results to console
print(analysis_results)

# Write analysis results to a text file
with open(file_to_output, "w") as txtfile:
    txtfile.write(analysis_results)
