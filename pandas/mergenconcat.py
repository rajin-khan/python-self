import pandas as pd

bios = pd.read_csv('SELF-PYTHON/pandas/assets/bios.csv')
nocs = pd.read_csv('SELF-PYTHON/pandas/assets/noc_regions.csv')

#say we wanna combine the info of NOC with the bios NOC: (National Olympic Commitee)
# pd.merge(bios, nocs, on='NOC') #usually how you would wanna compare, but in our row, we're trying to make born country NOC from the other csv, so:
bios_new = pd.merge(bios, nocs, left_on='born_country', right_on='NOC', how='inner') #how specifies inner joins, outer joins, left joins, and right joins, like in SQL.
#let's now rename that region column to sth else:
bios_new.rename(columns={'region': 'born_country_full'}, inplace=True)
print(bios_new)

ban = bios[bios['born_country'] == "BAN"].copy() #creates a dataframe with just bangladeshi athlete's data
jpn = bios[bios['born_country'] == "JPN"].copy() #same for japan

#say we wanna create a new df with just bd and jap athletes. we could:
new_df = pd.concat([ban, jpn]) #appends top to bottom and create a new df
print(new_df)

#say we wanna combine results data with bios info
results = pd.read_csv('SELF-PYTHON/pandas/assets/results.csv')

combined_df = pd.merge(results, bios, on='athlete_id', how='left') #same as you learned in SQL.
print(combined_df)