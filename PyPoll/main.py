# Modules
import os
import csv


# Set path for file
#csvpath = os.path.join("election_data.csv")
csvpath = os.path.join("..","PyPoll","Resources","election_data.csv").replace("\\", "/")

Candidates = []
Candidate_list = []

counter = []
Candidate_index = []

vote_percentage = []

#with open(csvpath, encoding='utf-8') as csvfile:
with open(csvpath, ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #removing the header
    csv_header = next(csvreader)

    # extracting candidate names from the list to create candidate list
    for names in csvreader:
        Candidates.append(names[2])

    # Calcuating total votes
    total_vote_count =  len(Candidates)
    

    # removing duplicate names from the list and creating list of unique candidates
    Candidate_list = list(set(Candidates))   

    
    # Creating a list to track voting counts and setting the size of the list
    x = len(Candidate_list)
    for size in range(x):
        Candidate_index.append(int("0"))

    # counting number of votes per candidates and adding to the list
    # The total number of votes each candidate won
    for votes in Candidates:
        counter = Candidate_list.index(votes) 
        Candidate_index[counter] += 1

    # Calculating percentage of votes each candidate won
    for candidate_vote in range(x):
        vote_percentage.append("{:.3%}".format((Candidate_index[candidate_vote]/total_vote_count)))

    analysis=[]
    analysis = list(zip(Candidate_list,vote_percentage,Candidate_index))
    
    #Finding the winner of the election based on popular vote.
    winner_name = []
    for winner in analysis:
        if winner[2] == max(Candidate_index):
            winner_name.append(winner[0])
    
   
    # Printing Election Results to the Terminal
    print("Election Results")
    print("-------------------------------")
    print(f"Total Votes: {total_vote_count}")
    print("-------------------------------")
    for results in analysis:
        print(f"{results[0]}: {results[1]} ({results[2]})")
    print("-------------------------------")
    print(f"Winner : {winner_name[0]}")
    print("-------------------------------")
    
    #Exporting file to text file
    output_file = os.path.join("..","PyPoll","analysis","output_file.txt").replace("\\", "/")
    #output_file = os.path.join("output_file.txt")
    with open(output_file, "w") as datafile:
        
        print("Election Results",file=datafile)
        print("-------------------------------",file=datafile)
        print(f"Total Votes: {total_vote_count}",file=datafile)
        print("-------------------------------",file=datafile)
        
        for results in analysis:
            print(f"{results[0]}: {results[1]} ({results[2]})",file=datafile)
        print("-------------------------------",file=datafile)
        print(f"Winner : {winner_name[0]}",file=datafile)
        print("-------------------------------",file=datafile)