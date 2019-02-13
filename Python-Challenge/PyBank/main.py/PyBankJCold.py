import os
import csv
import numpy as np

csvpath = os.path.join('..', 'Resources', 'budgetdata.csv')

with open(csvpath, newline='') as csvfile:

# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset
    #You can use a set to remove duplicates, and then the len function to count the elements in the set:
    #len(set(new_words))

# The net total amount of "Profit/Losses" over the entire period
    #sum function
def unique(Datelist1)
    Datelist1 = [A:A]
        Datelist1 = num_periods.Colum[A:A].Count
       print (Datelist1).count


#The average of the changes in "Profit/Losses" over the entire period
    #(sum(profits/losses) / num_periods )
    #example from 3-7 Solved
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length

#The greatest increase in profits (date and amount) over the entire period
    #MAX function on column: used same as average but what to return?
def MAX(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total 

#The greatest decrease in losses (date and amount) over the entire period
    #MIN on column B



#Upload new file to folder

    #csvpath = os.path.join("output", filename)
    #with open(csvpath, "w") as csvfile:
   # fieldnames = ["last_name", "first_name", "ssn", "email"]
   # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
   # writer.writeheader()
   # writer.writerows(new_employee_data)