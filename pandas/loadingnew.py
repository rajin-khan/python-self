import pandas as pd

coffee = pd.read_csv('SELF-PYTHON/pandas/assets/coffee.csv') #we can also put URLS to certain files if we want (for example, maybe in a github repo, you go to the raw link of the file and then get the link from there)
#instead of csv files (which are popular), which take up a lot of space, more popular options are feather, or parquet
#for comparison, a csv file that is 30mb, is 10mb for feather, and 4 mb for parquet.

print(coffee.head())

results = pd.read_parquet('SELF-PYTHON/pandas/assets/results.parquet')
print(results.head())

olympics_data = pd.read_excel('SELF-PYTHON/pandas/assets/olympics-data.xlsx')
print(olympics_data.head())
#excel files take MUCH, MUCH LONGER to load and read.

#you could load up some data from one format in a dataframe, (let's use the coffee dataframe)
#then, you could convert it to another format using:
coffee.to_csv
#or maybe,
coffee.to_parquet