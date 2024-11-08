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

    

def parse_data():
  """Read zipcodes.txt and return a list of each row stored as a dictionary"""
  zipcodes = [] # store each row as a dictionary

  # Open the .txt file and specify tab as the delimiter
  with open('zipcodes.txt', 'r') as file:
      reader = csv.DictReader(file, delimiter='\t')
        
      # Read each row in the txt file
      for row in reader:
          zipcodes.append(row)  # Add each row (dictionary) to the list

  return zipcodes

def parse_states(zipcodes, states_file):
    """Parse states.txt and create a dictionary of cities by states contained in the txt file"""
    state_cities = {}

    with open(states_file, 'r') as file:
        states = {line.strip() for line in file}

    for entry in zipcodes:
        state = entry['State']
        city = entry['City']

        if state in states:
            if state not in state_cities:
                state_cities[state] = set()
            state_cities[state].add(city)

    return state_cities
      
if __name__ == "__main__": 
    start_time = time.perf_counter()  # Do not remove this line
    '''
    Inside the __main__, do not add any codes before this line.
    -----------------------------------------------------------
    '''
    
    # parse all the data from zipcodes.txt
    zipcodes = parse_data()

    # parse all the states in zipcodes
    state_cities = parse_states(zipcodes, 'states.txt')


    '''
    Inside the __main__, do not add any codes after this line.
    ----------------------------------------------------------
    '''
    end_time = time.perf_counter()
    # Calculate the runtime in milliseconds
    runtime_ms = (end_time - start_time) * 1000
    print(f"The runtime of the program is {runtime_ms} milliseconds.")  