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
  zip_coords = []

  # Read the list of zip codes line by line
  with open(zips_file, 'r') as file:
      zips = [line.strip() for line in file]  # Use a list to keep the same order as its read

  # Create a dictionary for efficient lookup from zipcodes data
  zip_data = {
      entry['Zipcode']: f"{entry['Lat']} {entry['Long']}"
      for entry in zipcodes
  }

  # Go through zips in the order of zips.txt and add lat-lon coords if they exist
  for zip_code in zips:
      if zip_code in zip_data:
          zip_coords.append((zip_code, zip_data[zip_code]))

  return zip_coords

def lat_lon(zip_coords, output_file):
    """Write zip codes with their latitude and longitude to the output file."""
    with open(output_file, 'w') as file:
        for _, coords in zip_coords:
            file.write(f"{coords}\n")

def parse_cities(zipcodes, cities_file):
    """Parse cities.txt and create a dictionary of states that contain that city"""
    with open(cities_file, 'r') as file:
        cities = [line.strip().upper() for line in file]

    city_states = {}

    # Create a dictionary where cities are the key and the value is the set of states
    # containing the city
    for entry in zipcodes:
        city = entry['City']
        state = entry['State']
        if city in cities:
            if city not in city_states:
                city_states[city] = set()
            city_states[city].add(state)

    # Sort the output
    for city in city_states:
        city_states[city] = sorted(city_states[city])

    return city_states

def write_city_states(city_states, output_file):
    """Write states containing the city to the output file."""
    with open(output_file, 'w') as file:
        for states in city_states.items():
            file.write(f"{states}\n")


      
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

    # parse all latitude and longitude coords
    zip_coords = parse_zips(zipcodes, 'zips.txt')

    # write the lat-lon coords of the zip code to a text file
    lat_lon(zip_coords, 'LatLon.txt')

    # parses all cities from cities.txt and find states with the city in them
    city_states = parse_cities(zipcodes, 'cities.txt')

    # writes the states containing the city
    write_city_states(city_states, 'CityStates.txt')





    print(f"Parsed zipcodes: {zipcodes[:5]}")  # Print the first 5 entries to check

    # Step 2: Parse all states in zipcodes
    state_cities = parse_states(zipcodes, 'states.txt')
    print(f"State cities mapping: {dict(list(state_cities.items())[:5])}")  # Sample first 5

    # Step 3: Find all common cities and write them to a text file
    common_cities(state_cities, 'CommonCityNames.txt')

    # Step 4: Parse latitude and longitude coords
    zip_coords = parse_zips(zipcodes, 'zips.txt')
    print(f"Zip coordinates: {zip_coords[:5]}")  # Print the first 5 entries

    # Step 5: Write the lat-lon coords of the zip code to a text file
    lat_lon(zip_coords, 'LatLon.txt')

    # Step 6: Parse cities from cities.txt and find states with the city in them
    city_states = parse_cities(zipcodes, 'cities.txt')
    print(f"City-states dictionary: {dict(list(city_states.items())[:5])}")  # Sample first 5 entries

    # Step 7: Write the states containing the city to CityStates.txt
    write_city_states(city_states, 'CityStates.txt')
    print("CityStates.txt has been written.")


    '''
    Inside the __main__, do not add any codes after this line.
    ----------------------------------------------------------
    '''
    end_time = time.perf_counter()
    # Calculate the runtime in milliseconds
    runtime_ms = (end_time - start_time) * 1000
    print(f"The runtime of the program is {runtime_ms} milliseconds.")  