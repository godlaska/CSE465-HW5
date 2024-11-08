import time
import csv

"""
  Homework#5

  Add your name here: Keigen Godlaski

  You are free to create as many classes within the hw5.py file or across 
  multiple files as you need. However, ensure that the hw5.py file is the 
  only one that contains a __main__ method. This specific setup is crucial 
  because your instructor will run the hw5.py file to execute and evaluate 
  your work.

"""
"""
1- => Lambda was used in line/s: ............
2- => Filter or map was used in line/s: ...........
3- => yield was used in line/s: .........
"""

    

def parseData():
  zipcodes = [] # store each row as a dictionary

  # Open the .txt file and specify tab as the delimiter
  with open('zipcodes.txt', 'r') as file:
      reader = csv.DictReader(file, delimiter='\t')
        
      # Read each row in the txt file
      for row in reader:
          zipcodes.append(row)  # Add each row (dictionary) to the list

  return zipcodes

if __name__ == "__main__": 
    start_time = time.perf_counter()  # Do not remove this line
    '''
    Inside the __main__, do not add any codes before this line.
    -----------------------------------------------------------
    '''
    
    zipcodes = parseData()

    for entry in zipcodes:
      print(entry['City'])  # Access the 'City' field in each dictionary

    '''
    Inside the __main__, do not add any codes after this line.
    ----------------------------------------------------------
    '''
    end_time = time.perf_counter()
    # Calculate the runtime in milliseconds
    runtime_ms = (end_time - start_time) * 1000
    print(f"The runtime of the program is {runtime_ms} milliseconds.")  