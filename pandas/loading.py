#load data from a csv
#data gets loaded in a data frame

import pandas as pd

df = pd.read_csv('assets/pokemon_data.csv') #you can load up other files too, with read_json, excel, html, other stuff
#we can even load a tab separated text file, and for that we'd still use read csv, but specify a delimiter, in this case, a tab.
#so pd.read_csv('path/to/file.txt', delimiter='\t') (delimiter could be anything)

print(df) #hard to print that many rows and cols, so we do sth else
print(df.head(3)) #prints the first 3 rows
print(df.tail(3)) #prints the last 3 rows