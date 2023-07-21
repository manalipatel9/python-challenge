from pathlib import Path
import csv

#defines the path in which the file is in 
file_path=Path("Resources/budget_data.csv")

#define variables outside of loop
months=0
tot_prof_loss=0
prev_prof_loss=0
change_prof_loss=[]
GreatInc=[]
GreatDec=[]
date=[]

#this will iterate using the for loop to print each line in the file
with open(file_path,'r') as data_file:
    reader=csv.reader(data_file) 
    #stores and skips the header line 
    header=next(reader) 
    #loops through all the rows in the csv file and will print it out
    # for row in reader: 
    #     print(row)
        #loops through all the csv file rows 
    for row in reader:
        #counts all the months in the data set
        months+=1
        #calculates the profit/loss and makes it an integer(no decimals)
        tot_prof_loss+=int(row[1])
        #calculate the changes in profits/losses
        net_change=int(row[1])-prev_prof_loss
         #update the prev_prof_loss to the next row
        prev_prof_loss=int(row[1])
        change_prof_loss+=[net_change]
        #get the greatest increase date and profits 
        great_inc_date=change_prof_loss.index(max(change_prof_loss))
        great_inc_prof=max(change_prof_loss)
        #get the greatest decrease date and profits
        great_dec_date=change_prof_loss.index(min(change_prof_loss))
        great_dec_prof=min(change_prof_loss)

        print(great_inc_date)
        print(great_inc_prof)
    #calculates the average change in profits and losses
    avg_change=sum(change_prof_loss)/len(change_prof_loss)
    #for i in range(1,len())

#prints the the data that was calculated above     
print("Financial Analysis")
print("------------------------------")
print("Total Months:", months)
print("Total: $", tot_prof_loss)
print("Average Change: $", avg_change)
print("Greatest Increase in Profits:", great_inc_date, "$",great_inc_prof)
print("Greatest Decrease in Profits:", great_dec_date, "$",great_dec_prof)

new_file_path=Path("Resources/PyBankOutput.txt")
# Step 1: Open the file in write mode
with open(new_file_path, "w") as file:
    # Step 2: Write content to the file
    file.write("Financial Analysis \n")
    file.write("------------------------------")
    file.write("\n")
    file.write("Total Months: " + str(months))
    file.write("\n")
    file.write("Total: $ " + str(tot_prof_loss))
    file.write("\n")
    file.write("Average Change: $ " + str(avg_change)) 
    file.write("\n")
    file.write("Greatest Increase in Profits: " + str(great_inc_date) + " $" + str(great_inc_prof))
    file.write("\n")
    file.write("Greatest Decrease in Profits: " + str(great_dec_date) + " $" + str(great_dec_prof))