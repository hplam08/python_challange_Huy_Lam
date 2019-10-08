import csv 
import os

budget_csv = os.path.join("Resources", 'budget_data.csv')

total_months = 0
total_profit = 0
value = 0 
change = 0
dates = []
profit = []

# open and read CSV file
with open(budget_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    
    #read the header row
    csv_header = next(csvreader)
    
    #read the first row
    first_row = next(csvreader)
    total_months = total_months + 1
    total_profit = total_profit + 1
    value = int(first_row[1])
    
    #Loop through each row of data after header and the first row
    for row in csvreader:
        dates.append(row[0])
        change = int(row[1])-value
        profit.append(change)
        value = int(row[1])
        
        #Total number of months 
        total_months = total_months + 1
        
        #Total profit 
        total_profit = total_profit + int(row[1])
    
    #Calculating largest increase in profit: 
    largest_increase = max(profit)
    largest_index = profit.index(largest_increase)
    largest_date = dates[largest_index]
    
    #Calculating largest decrease in profits:
    largest_decrease = min(profit)
    worst_index = profit.index(largest_decrease)
    worst_date = dates[worst_index]
    
    #Calculating average change:
    avg_change = sum(profit)/len(profit)
    
#Print statements:
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_profit)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {largest_date} (${str(largest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(largest_decrease)})")

#exporting to .txt file

output = open('output.txt', 'w')

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f'Total Months: {str(total_months)}')
line4 = str(f"Total: ${str(total_profit)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {largest_date} (${str(largest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(largest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))