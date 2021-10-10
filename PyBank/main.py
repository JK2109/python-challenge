# Modules
import os
import csv


# Set path for file
csvpath = os.path.join("..","Resources","budget_data.csv").replace("\\", "/")


# Lists to store datas
date = []
profit_losses = []
monthly_changes_col = []


#with open(csvpath, encoding='utf-8') as csvfile:
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    
    #Assignig variables
    
    row = 1
    previous_month = 0
    Total = 0
    monthly_changes = 0

    for months in csvreader:
        
        date.append(months[0])
        profit_losses.append(months[1])
        
        #Calculating the net total amount over the entire period
        Total = int(months[1]) + Total
        

        if row == 1: 
            #monthly_changes = 0     #Handling of the first row
            previous_month = int(months[1])
            row = row + 1
            
        else:
            current_month = int(months[1])
            
            #Calculating the monthly differences by subtracting previous month p&l from current month p&l
            monthly_changes = current_month - previous_month  
            previous_month = current_month
            
        monthly_changes_col.append(monthly_changes)
            
    #adding the monthly_changes to the existing list using zip function
    new_list = zip(date,profit_losses,monthly_changes_col)
    

    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in profits (date and amount) over the entire period
    greatest_inc_date =[]
    greatest_dec_date =[]
    greatest_inc_amount =[]
    greatest_dec_amount =[]

    for new_months in new_list:
        if new_months[2] == max(monthly_changes_col):
            greatest_inc_date.append(new_months[0])
            greatest_inc_amount.append(new_months[2])

        elif new_months[2] == min(monthly_changes_col):
            greatest_dec_date.append(new_months[0])
            greatest_dec_amount.append(new_months[2])

    

    #Calculating the number of months by counting the number of rows
    month_count = len(date)

    #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    monthly_total = sum(monthly_changes_col)
    monthly_average = round(monthly_total/(month_count-1),2) #subtracting by 1 from overall row count to calculate average of changes 
    

    
    
    #Printing Summarized Analysis
    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {month_count}")
    print(f"Total ${Total}")
    print(f"Average Change: ${monthly_average}")
    print(f"Greatest Increase in Profits: {(greatest_inc_date[0])} (${greatest_inc_amount[0]})")
    print(f"Greatest Decrease in Profits: {greatest_dec_date[0]}(${greatest_dec_amount[0]})")

#Exporting file to text file
#with open("output_file.txt", "w") as datafile:
    
    