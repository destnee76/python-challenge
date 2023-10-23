import os
import csv


# Read CSV path
csvpath = os.path.join(".","Resources","budget_data.csv")
txtpath = os.path.join(".","analysis","budget_analysis.txt")

# Variables
ttl_mths = 0
overall_ttl = 0
value = 0
change = 0
dates = []
profits = []

#Opening and reading the CSV file
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Reading the header row
    csv_header = next(csvreader)

    #Reading the first row (so that we track the changes properly)
    first_row = next(csvreader)
    ttl_mths  += 1
    overall_ttl += int(first_row[1])
    value = int(first_row[1])
    
    # Line by line
    for row in csvreader:
        dates.append(row[0])
        
        # Changes
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        # Total Months
        ttl_mths += 1

        # Profit/Losses total
        overall_ttl = overall_ttl + int(row[1])

  
    greatest_increase = max(profits)
    max_incr = profits.index(greatest_increase)
    max_incr_date = dates[max_incr]

    greatest_decrease = min(profits)
    max_decr = profits.index(greatest_decrease)
    max_decr_date = dates[max_decr]

    avg_change = sum(profits)/len(profits)
    

output = (
    f"Financial Analysis\n"
    f"---------------------\n"
    f"Total Months: {str(ttl_mths)}\n"
    f"Total: ${str(overall_ttl)}\n"
    f"Average Change: ${str(round(avg_change,2))}\n"
    f"Greatest Increase in Profits: {max_incr_date} (${str(greatest_increase)})\n"
    f"Greatest Decrease in Profits: {max_decr_date} (${str(greatest_decrease)})")

with open(txtpath,'w') as txtout:
        print(output)
        txtout.write(output)


# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)