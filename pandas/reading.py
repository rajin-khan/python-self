import pandas as pd

df = pd.read_csv('SELF-PYTHON/pandas/assets/pokemon_data.csv')

#read just the col headers
print(df.columns)

#read specific cols
print(df['Name'])
#or if you don't wanna print all the cols,
print(df['Name'][0:5])
#you can target specific cols together too,
print(df[['Name', 'Type 1', 'HP']][0:5])

#read specific rows
print(df.iloc[1]) #integer location, so we get all the data from the row in that index
#read multiple rows
print(df.iloc[1:4])

#read a specific location (rows, cols)
print(df.iloc[2, 1])

#to access any data row by row
for index, row in df.iterrows():
    print(index, row['Name'])
    
#in addition to iloc, we have df.loc, which can narrow down our location searching with conditions
print(df.loc[df['Type 1'] == 'Fire'])
print(df.loc[df['Type 1'] == 'Grass'])

#to get basic stats from the table easily, use:
print(df.describe()) #this gives us stuff like q1, q2, q3, mean, standard dev, max, etc in a table.

#sorting output
print(df.sort_values('Name'))
df.sort_values('Name', ascending=False) #shows it in descending order, ascending is default
df.sort_values(['Type 1', 'HP'], ascending=[1,0]) #can sort by multiple params