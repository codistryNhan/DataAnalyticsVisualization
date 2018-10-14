import os
import csv

def average(list_of_num):
  sum = 0
  for num in list_of_num:
    sum += num

  return sum / len(list_of_num)

def return_greatest_increase(list_of_num):
  max = 0;
  for num in list_of_num:
    if(num > max):
      max = num

  return max

def return_greatest_decrease(list_of_num):
  max_decrease = 0
  for num in list_of_num:
    if(num < max_decrease):
      max_decrease = num

  return max_decrease

file_path = os.path.join('Resources', 'budget_data.csv')

with open(file_path, newline="") as file_object:
  file = csv.reader(file_object)

  # Total number of months
  total_months = 0

  # Total net amount of "Profit/Losses"
  net_amount = 0

  # Average Change in "Profit/Losses" between months over entire period
  last = 0
  change_list = []
  average_change = 0

  # Greatest Increase in profits (date and amount) over the entire period
  max_increase = 0

  # Greatest Decrease in losses (date and amount) over the entire period
  max_decrease = 0

  # Get rid of header line
  file.__next__();

  for row in file:
    num = int(row[1])

    total_months += 1
    net_amount += num

    if (last == 0):
      last = num
    else:
      change = num - last
      last = num
      change_list.append(change)

  average_change = int(average(change_list))
  max_increase = int(return_greatest_increase(change_list))
  max_decrease = int(return_greatest_decrease(change_list))

  print(total_months)
  print(net_amount)
  print(average_change)
  print(max_increase)
  print(max_decrease)
