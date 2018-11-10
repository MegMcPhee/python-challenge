import os
import csv

csvpath = os.path.join('..', 'Data','election_data.csv')

rows = []
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i, row in enumerate(csvreader):
        if i==0:
            header = row
        else:
            rows.append(row)
    
    total_votes = 0
    votes_dict = {}
    khan_votes = 0
    
    for i in range(len(rows)):
    #Total Votes
        total_votes += 1
        candidate = rows[i][2]
    
        if candidate in votes_dict:
            votes_dict[candidate] += 1
        else:
            votes_dict[candidate] = 1

#    print(votes_dict)

max_votes = 0
winner = " "
    
#Print Everything
print(f'Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')
for key, value in votes_dict.items():
    print(f'{key}: {value/total_votes*100:.3f}% ({value})')
    if value > max_votes:
        max_votes = value
        winner = key
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

#Create text file
file_to_output = os.path.join('..', 'Data', 'ElectionResults.txt')
with open(file_to_output, "w") as txt_file:
    txt_file.write(f'Election Results\n')
    txt_file.write('-------------------------\n')
    txt_file.write(f'Total Votes: {total_votes}\n')
    txt_file.write('-------------------------\n')
    for key, value in votes_dict.items():
        txt_file.write(f'{key}: {value/total_votes*100:.3f}% ({value})\n')
        if value > max_votes:
            max_votes = value
            winner = key
    txt_file.write('-------------------------\n')
    txt_file.write(f'Winner: {winner}\n')
    txt_file.write('-------------------------\n')