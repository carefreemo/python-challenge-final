# Step 1a: Print these headers
print("Election Results")
print("----------------------------")
# Step 1b: Import the csv file and prep it to be read
# Import the csv library
import csv 

# This code displays the file path of the csv file
with open ("PyPoll/Resources/election_data.csv", newline = '') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

# This is how you read the header in the csv files... not all CSVs have headers
    # csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

# This is how you reader each row in the csv file (will not use because there is a lot of data)
    # for row in csvreader:
        # print(row)

# Step 2: Find the total number of months included in the dataset
    next(csvreader)
    data = list (csvreader)
    row_count = len(data)

print(f"Total Votes: {row_count}")

print("----------------------------")

# Step 3: Find a complete list of candidates who received votes
candidateslist = list ()
candidatesvote = list()
for vote in range (0, row_count):
    candidate = data[vote][2]
    candidatesvote.append(candidate)
    if candidate not in candidateslist:
        candidateslist.append(candidate)
candidatecount = len(candidateslist)

# Step 4: Find the percentage of votes each candidate won and the total number of votes each candidate won
votes = list()
percentage = list ()
for x in range (0, candidatecount):
    name = candidateslist[x]
    votes.append(candidatesvote.count(name))
    votepercentage = votes[x]/row_count
    percentage.append(votepercentage)

for p in range (0,candidatecount):
    print(f"{candidateslist[p]}: {percentage[p]:.3%} ({votes[p]})")

print("----------------------------")

# Step 5: Find the winner based on popular vote
popularwinner = votes.index(max(votes))

print(f"Winner: {candidateslist[popularwinner]}")

print("----------------------------")

# Step 6: Now print the PyPoll Results into text
print("Election Results", file=open("PyPoll.txt", "a"))
print("----------------------------", file=open("PyPoll.txt", "a"))
print(f"Total Votes: {row_count:,}", file=open("PyPoll.txt", "a"))
print("----------------------------", file=open("PyPoll.txt", "a"))
for p in range (0,candidatecount): 
    print(f"{candidateslist[p]}: {percentage[p]:.3%} ({votes[p]:,})", file=open("PyPoll.txt", "a"))
print("----------------------------", file=open("PyPoll.txt", "a"))
print(f"Winner: {candidateslist[popularwinner]}", file=open("PyPoll.txt", "a"))
print("----------------------------", file=open("PyPoll.txt", "a"))