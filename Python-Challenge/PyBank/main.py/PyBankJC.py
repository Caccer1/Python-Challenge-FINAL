import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#list
total_months = []
total_profit = []
monthly_profit_change = []

#variables
#month_count = 0
#total_profit = 0
#average_change = 0


with open(csvpath, newline='', encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_head = next(csvreader)

      #writer file - giving 1) syntax error and 2) indent error and 3) string error
   # with open (csvpath, 'newPyBankanswers', 'w') as new_file:
       # csv_writer = csv.writer(new_file, delimiter=",")

    #sum function

    for row in csvreader:

       total_months.append(row[0])
       total_profit.append(int(row[1]))

    for i in range(len(total_profit)-1):

       monthly_profit_change.append(total_profit[i+1]-total_profit[i])

max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1

 

# Print Statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

with open(csvfile, "w") as txtFile:
   txtFile.write(print)
#TpeError: expected str, bytes or os.PathLike object, not _io.TextIOWrapper
       
       


       
       
        #did work is above - didn't work is below
        #You can use a set to remove duplicates, and then the len function to count the elements in the set:
        #len(set(budgetdata)) - using len and set to calculate unique rows but that isn't working
        #def unique(Datelist1

    #(sum(profits/losses) / num_periods )
   
    #example from 3-7 Solved
    #def average(numbers):
    #      length = len(numbers)
    #  total = 0.0
    # for number in numbers:
     #    total += number
     #return total / length

#The greatest increase in profits (date and amount) over the entire period
    #MAX function on column: used same as average but what to return?
#def MAX(numbers):
    #length = len(numbers)
    #total = 0.0
    #for number in numbers:
     #   total += number
    #return total 