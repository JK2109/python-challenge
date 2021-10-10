# Modules
import os
import csv


# Set path for file
csvpath = os.path.join("election_data.csv")
#csvpath = os.path.join("..","Resources","election_data.csv").replace("\\", "/")

vote_ID = []
Candidate = []
name_list = []

count_khan = 0
count_correy = 0
count_li = 0
count_otooley = 0

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #removing the header
    csv_header = next(csvreader)


    for votes in csvreader:
        vote_ID.append(votes[0])
        Candidate.append(votes[2])
        
        #Had to break up the program in two steps where first step is to get the unique names and print
        #Once unique names are identified, run the program to run the analysis
        
    
    
    #     To identify unique candidate names
    #     for names in Candidate:
    #         if names not in name_list: 
    #             name_list.append(names)
      
    # print(name_list)

        if votes[2] == "Khan":
            count_khan = count_khan + 1
        elif votes[2] =="Correy":
            count_correy = count_correy + 1
        elif votes[2] =="Li":
            count_li = count_li + 1
        elif votes[2] =="O'Tooley":
            count_otooley = count_otooley + 1

    

    vote_count =  len(vote_ID)

    percentage_khan = round((count_khan / vote_count)*100,2)
    percentage_correy = round((count_correy / vote_count)*100,2)
    percentage_li = round((count_li  / vote_count)*100,2)
    percentage_ottoley = round((count_otooley / vote_count)*100,2)

    # Printing Results
    print("Election Results")
    print("--------------------------")
    print(f"Khan : {percentage_khan}%  ({count_khan})")
    print(f"Khan : {percentage_correy}%  ({count_correy})")
    print(f"Khan : {percentage_li}%  ({count_li})")
    print(f"Khan : {percentage_ottoley}%  ({count_otooley})")
    print("--------------------------")
    #print(f"Winner : {}")
    print("--------------------------")