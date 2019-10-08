import csv
import os 

election_data = os.path.join('..', 'Resources', 'election_data.csv')

#intializing variables 

candidates = []
num_votes = []
percent_vote = []
total_votes = 0

#read csv 

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
            
    for votes in num_votes:
        percentage = (votes/total_votes)*100
        percentage = round(percentage)
        percentage = "%.f%%" % percentage
        percent_vote.append(percentage)
    
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]
    
#print results: 

print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_vote[i])} ({str(num_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")


#exporting to a .txt file:
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_vote[i])} ({str(num_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))