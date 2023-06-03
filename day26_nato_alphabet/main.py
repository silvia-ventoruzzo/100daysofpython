# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

import os
import pandas as pd

os.chdir('day26_nato_alphabet/')

df = pd.read_csv('nato_phonetic_alphabet.csv')
dct = {row['letter']:row['code'] for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input('Enter word:')
spelling = [dct[letter.upper()] for letter in word]
print(spelling)
