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

    # Use dictionary comprehension to build state_cities instead of a for-loop
    # Dictionary comprehension was assisted by ChatGPT
    state_cities = {
        state: {entry['City'] for entry in zipcodes if entry['State'] == state}
        for state in states
    }

    return state_cities

def common_cities(state_cities, output_file):
  if not state_cities:
      return # if there's no states given, return nothing

  # find the common cities between each city set
  common_cities = set.intersection(*state_cities.values())

  # open and write CommonCityNames.txt with all common cities
  with open(output_file, 'w') as file:
      for city in sorted(common_cities):
          file.write(city + '\n')

def parse_zips(zipcodes, zips_file):
  """Parse zips.txt and create a dictionary of zipcodes in states contained in the txt file"""
  zip_coords = {} # use a set so there's not duplicate lat-lon caused by repeated zipcodes

  # Read zipcodes from zips.txt
  with open(zips_file, 'r') as file:
        zips = {line.strip() for line in file}

  # Use dictionary comprehension to map each zipcode with its lat lon coords
  zip_coords = {
    entry['Zipcode']: f"{entry['Lat']} {entry['Long']}"
    for entry in zipcodes
    if entry['Zipcode'] in zips and entry['Zipcode'] not in zip_coords
  }
  
  return zip_coords

def lat_lon(zip_coords, output_file):
    """Write zip codes with their latitude and longitude to the output file."""
    with open(output_file, 'w') as file:
        for zip_code, coords in zip_coords.items():
            file.write(f"{coords}\n")

      
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

    # find all common cities and write them to a text file
    common_cities(state_cities, 'CommonCityNames.txt')

    zip_coords = parse_zips(zipcodes, 'zips.txt')

    lat_lon(zip_coords, 'LatLon.txt')


    '''
    Inside the __main__, do not add any codes after this line.
    ----------------------------------------------------------
    '''
    end_time = time.perf_counter()
    # Calculate the runtime in milliseconds
    runtime_ms = (end_time - start_time) * 1000
    print(f"The runtime of the program is {runtime_ms} milliseconds.")  