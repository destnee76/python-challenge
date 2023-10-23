import os
import csv


# Read CSV path
csvpath = os.path.join(".","Resources","election_data.csv")
txtpath = os.path.join(".","analysis","election_analysis.txt")

#Variables
ttl_votes = 0 
candidate_votes = {}
curr_candidate = ""
candidates = []
winning_candidate = ""
winning_count = 0


#Opening and reading the CSV file
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)

    # Looping through data rows
    for row in csvreader:
        ttl_votes = ttl_votes + 1
        curr_candidate = row[2]
        if curr_candidate not in candidates:
            candidates.append(curr_candidate)
            candidate_votes[curr_candidate] = 1
        else:               
            candidate_votes[curr_candidate] = candidate_votes[curr_candidate] + 1

    
    
with open(txtpath,'w') as txtout:
    print(
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {ttl_votes}\n"
    f"-------------------------\n")
    txtout.write(
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {ttl_votes}\n"
    f"-------------------------\n")
    
    for candidate in candidates:
        votes = candidate_votes[candidate]
        vote_percentage = votes/ttl_votes * 100
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        
        print(voter_output)
        txtout.write(voter_output)
        if(votes > winning_count):
            winning_candidate = candidate
            winning_count = votes
    print("--------------------------")
    txtout.write("--------------------------\n")
    print(f"Winner: {winning_candidate}")
    txtout.write(f"Winner: {winning_candidate}")



# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------        