import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

#list
total_votes = []
candidates_list = []
percent_votes = []



with open(csvpath, newline='', encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_head = next(csvreader)
    
    for row in csvreader:
      total_votes.append(row[0])
      #total_votes =candidates_list.nunique(candidates_list)
      
      #trying to count total votes % like n wrestling function but error index is out of range
      #total_votes = (int(candidates_list[2]) / total_votes) * 100

#1 print total number of votes case
print (f"Total Votes: {len(total_votes)}")
#2 print candidate list
print (f"Correy, Khan, Li, O'Tooley")
#3 print % of votes by candidate
print(total_votes, "Correy")

#4 print # of votes by candidate
#CorreyVotes = []
#CorreyVOtes not defined
#CorreyVotes = CorreyVotes.count(row[2], str("Correy")) 
#print(CoreyVotes).count
#attribute error - has no attribute
#CorreyVotes = CorreyVotes.csvreader['Candidate'].value_counts("Correy")[2]
#print(CorreyVotes)
print(f"Correy Total Votes are:", count())


#5 Print who wins the popular vote
print (f"Khan wins the popular vote!")

#1* The total number of votes cast
# determine unique values in a column
#column_x.nunique()   # count the number of unique values
#column_x.unique()    # return the unique values
#column_x.nunique()
#print

#2* A complete list of candidates who received votes

#3* The percentage of votes each candidate won
  #winPercent = (int(wrestlerData[1]) / totalMatches) * 100

#4* The total number of votes each candidate won

#5* The winner of the election based on popular vote.

# Write updated data to csv file
#csvpath = os.path.join("output", filename)
#with open(csvpath, "w") as csvfile:
   # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
   # writer.writeheader()
   # writer.writerows(new_employee_data)





