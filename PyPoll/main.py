#import necesarry libraries that are needed for code 
from pathlib import Path
import csv 

#defines the path for the file 
file_path=Path("Resources/election_data.csv")

#defines the variables
tot_votes=0
Charles_votes=0
Diana_votes=0
Raymon_votes=0
winner=0
candidate_options=[]
candidate_votes={}

#iterate using a for loop to print the csv file
with open(file_path,'r') as file:
    reader=csv.reader(file)
    #stores and skips the header line 
    header=next(reader) 
    for row in reader:
        # print(row)
    #counts the total votes
        tot_votes+=1
        if row[2]== "Charles Casper Stockham":
            Charles_votes+=1
        elif row[2]=="Diana DeGette":
            Diana_votes+=1
        elif row[2]=="Raymon Anthony Doane":
            Raymon_votes+=1
    #calculates the percent of votes each candidate got 
    charles_per=(Charles_votes/tot_votes)*100
    diana_per=(Diana_votes/tot_votes)*100
    raymon_per=(Raymon_votes/tot_votes)*100
    #will make the value only have 3 decimals places 
    charles_per=round(charles_per,3)
    diana_per=round(diana_per,3)
    raymon_per=round(raymon_per,3)
    #gets the winner of the election
    # winner=

#prints the data that was calculated above$
print("Election Results")
print("----------------------------")
print("Total Votes: ", tot_votes)
print("----------------------------")
print("Charles Casper Stockham:", charles_per,"% (", Charles_votes, ")")
print("Diana DeGette:", diana_per,"% (", Diana_votes, ")")
print("Raymon Anthony Doane:", raymon_per,"% (", Raymon_votes, ")")
print("----------------------------")
print("Winner:", )

#creates a .txt file with the output 
new_file_path=Path("Resources/PyPoll.txt")
with open(new_file_path, 'w') as file:
    file.write("Election Results")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write("Total Votes: " + str(tot_votes))
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write("Charles Casper Stockham: " + str(charles_per) + "% (" + str(Charles_votes) + ")") 
    file.write("\n")
    file.write("Diana DeGette: "  + str(diana_per) + "% (" + str(Diana_votes) + ")") 
    file.write("\n")
    file.write("Raymon Anthony Doane: " + str(raymon_per) + "% (" + str(Raymon_votes) + ")") 
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write("Winner:", )