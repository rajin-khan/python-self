import pandas as pd

bios = pd.read_csv('SELF-PYTHON/pandas/assets/bios_new.csv')

#say we wanna know what the top cities for the olympic athletes to come from are, we could do:
print(bios['born_city'].value_counts())

#we can filter and then do value counts too:
print(bios[bios['born_country']=="BAN"]['born_region'].value_counts())

#sometimes it's useful to group data together
coffee = pd.read_csv('SELF-PYTHON/pandas/assets/coffee_new.csv')

print(coffee.groupby(['Coffee Type'])['Units Sold'].sum())
coffee.groupby(['Coffee Type'])['Units Sold'].mean()

#you can even group by multiple cols:
coffee.groupby(['Coffee Type', 'Day'])['Units Sold'].sum()


#we can achieve multiple aggregation outputs even more concisely, like this:
print(coffee.groupby(['Coffee Type']).agg({'Units Sold': 'sum', 'price': 'mean'})) #use the .agg function, and pass in a dictionary, of the col name, and the agg you wanna do (sum, mean, etc)

#similar to groupby, we have pivot tables, which allow us to view our data completely differenty:
pivot = coffee.pivot(columns='Coffee Type', index='Day', values='revenue')
print(pivot)

#now we can perform multiple actions on this df called pivot
pivot.sum() #total revenue from coffee sold by type
pivot.sum(axis=1) #total rev for each day

#maybe we wanna sort by the year they were born:
bios['born_date'] = pd.to_datetime(bios['born_date']) #covert it to datetime format
print(bios.groupby(bios['born_date'].dt.year)['name'].count())

#we could use the resetindex method to make it look more nice, like a table, and also to make it possible to use sort on it.
print(bios.groupby(bios['born_date'].dt.year)['name'].count().reset_index().sort_values('name', ascending=False))