import pandas as pd

bios = pd.read_csv('SELF-PYTHON/pandas/assets/bios.csv')

print(bios.head())
print(bios.info())

print(bios.loc[bios['height_cm'] > 215]) #print based on a condition
print(bios.loc[bios['height_cm'] > 215, ['name','height_cm']]) #same thing, just specify columns you wanna show.

#there is a shorthand syntax for this,
print(bios[bios['height_cm'] > 215]) #achieves the same effect, 
print(bios[bios['height_cm'] > 215], ['name', 'height_cm']) #same thing, just specifying the columns.

print(bios[(bios['height_cm'] > 215) & (bios['born_country'] == 'USA')]) #combining two conditions with logical ops

print(bios[bios['name'].str.contains("Rajin", case=False)]) #more interesting filtering, example of regex filtering (regular expression, maybe look up later)

print(bios.query('born_country == "BAN"'))