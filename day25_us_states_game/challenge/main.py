# Count of squirrels by fur color
import os
import pandas as pd

os.chdir('./day25_us_states_game/challenge/')

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

variable = 'Primary Fur Color'
squirrel_count = data[variable].value_counts().to_frame(name='Count').reset_index(names=variable)
squirrel_count.to_csv('squirrel_count.csv')