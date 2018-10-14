import os
import csv

# Create a function to determine max
def maxVotes(list_of_dict):
  max = 0
  winner = ""

  for dict in list_of_dict:
    if (dict['votes'] > max):
      max = dict['votes']
      winner = dict['name']

  return winner

file_path = os.path.join("Resources", "election_data.csv")

with open(file_path, newline='') as file_object:
  file = csv.reader(file_object)

  # Total number of votes cast
  total_votes = 0

  # List of candidates who received votes
  candidate_list = []

  # Total number of votes each candidate won
  candidate_dict_list = []

  # Winner of the election based on popular vote
  winner = ""

  # Ignore header
  file.__next__();

  # Loop through file
  for row in file:
    total_votes += 1

    # If candidate's name is not a key in a dictionary
    # we'll add it to the dictionary and initilize it with the value 1
    # we'll also append the names onto a list
    '''if not (row[2] in candidate_dict):
      candidate_dict[row[2]] = 1
      candidate_list.append(row[2])
    else:
      candidate_dict[row[2]] += 1'''
    if not (row[2] in candidate_list):
      candidate_dict = {}
      candidate_dict['name'] = row[2]
      candidate_dict['votes'] = 1
      candidate_list.append(row[2])
      candidate_dict_list.append(candidate_dict)
    else:
      for dict in candidate_dict_list:
        if dict['name'] == row[2]:
          dict['votes'] += 1


  winner = maxVotes(candidate_dict_list)

  print(f"Vote Counts: {total_votes}")
  print(f"List of Candidates: {candidate_list}")
  print(f"Candidate Vote Counts: {candidate_dict_list}")

  # Print Percentage of Votes
  for candidate in candidate_dict_list:
    print(f"{candidate['name']}: {int( (candidate['votes']/total_votes) * 100 ) }%")

  print(f"Winner: {winner}")
