import pandas as pd
import numpy as np

coffee = pd.read_csv('SELF-PYTHON/pandas/assets/coffee.csv')

#say we had some null values (which we don't, so we'll insert it):
coffee.loc[[0, 1], 'Units Sold'] = np.nan #once again, making use of numpy helper functions.

#we can view the info and it'll show how many items in each col are non null now:
print(coffee.info())

#we can also view the number of null items in each row like this:
print(coffee.isna().sum())

#we can fill all the null values like this.
#coffee = coffee.fillna(10000) 
#obviously not realistic, but if you get sth like this, and you need to fill it, you could use the mean to fill those values.
#perhaps like this:
coffee = coffee.fillna(coffee['Units Sold'].mean) #coffee['Units Sold].interpolate would try to predict the value by noticing patterns.

#we could even drop any row that has ANY null values, like this:
coffee.dropna() #of course you can assign it to the coffee df to make changes to the dataframe in this session, as above

#if you wanted to specifically drop units sold having null, you could do this:
coffee.dropna(subset=['Units Sold']) #remember to add inplace = True, or assign it back to dataframe with coffee = coffee.dropna(subset=['Units Sold'])
#alternatively, you could show the not null rows like this:
coffee[coffee['Units Sold'].notna()]

#to just get the null rows, we could:
coffee[coffee['Units Sold'].isna()]