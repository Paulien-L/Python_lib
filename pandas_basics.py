# https://rohitmidha23.github.io/Introduction-to-Pandas/

import pandas as pd
import numpy as np
import random

# SERIES

first_series = pd.Series([1,2,3, np.nan, "Hello!"])

# indexing series with custom index
first_series = pd.Series([1,2,3, np.nan, "Hello!"], index=['A','B','C','unknown','String'])

# dictionary to series
dict = {"Python" : "Best", "C" : "Only sawball likes this", "Java" : "Eh"}
second_series = pd.Series(dict)

second_series[["Python", "Java"]] # Selecting values
second_series.index # Index of series
second_series.values # Values of series
second_series.describe() # Describes series

# Series are mutable
second_series["Java"] = "OOP dream"
# Add new values
second_series["R"] = "Okay"

# DATA FRAMES
data = {'year': [1990, 1994, 1998, 2002, 2006, 2010, 2014],
        'winner': ['Germany', 'Brazil', 'France', 'Brazil','Italy', 'Spain', 'Germany'],
        'runner-up': ['Argentina', 'Italy', 'Brazil','Germany', 'France', 'Netherlands', 'Argentina'],
        'final score': ['1-0', '0-0 (pen)', '3-0', '2-0', '1-1 (pen)', '1-0', '1-0'] }
world_cup = pd.DataFrame(data, columns=['year', 'winner', 'runner-up', 'final score'])

# or using dictionaries
data_2 = [{'year': 1990, 'winner': 'Germany', 'runner-up': 'Argentina', 'final score': '1-0'},
          {'year': 1994, 'winner': 'Brazil', 'runner-up': 'Italy', 'final score': '0-0 (pen)'},
          {'year': 1998, 'winner': 'France', 'runner-up': 'Brazil', 'final score': '3-0'},
          {'year': 2002, 'winner': 'Brazil', 'runner-up': 'Germany', 'final score': '2-0'},
          {'year': 2006, 'winner': 'Italy','runner-up': 'France', 'final score': '1-1 (pen)'},
          {'year': 2010, 'winner': 'Spain', 'runner-up': 'Netherlands', 'final score': '1-0'},
          {'year': 2014, 'winner': 'Germany', 'runner-up': 'Argentina', 'final score': '1-0'}
         ]
world_cup = pd.DataFrame(data_2)
#print(world_cup.head(2), end="\n\n") # Prints header + first 2 rows
#print(world_cup.tail(2), end="\n\n") # Prints header + last 2 rows
#print(world_cup[2:4]) # Using slicing

# Write to csv
world_cup.to_csv("worldcup.csv")

# Read csv
world_cup = pd.read_csv("worldcup.csv", index_col=0) #read w/o index
print(world_cup) 
