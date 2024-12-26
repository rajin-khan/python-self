import pandas as pd

coffee = pd.read_csv('SELF-PYTHON/pandas/assets/coffee.csv')

coffee.sample(10) #gives you 10 random data from your table

print(coffee.loc[0]) #access specific data with loc[rows, cols] (or just any one of these values)
print(coffee.loc[[0, 1, 5]])#will only print row 0, 1, and 5

print(coffee.loc[5:12, ["Day", "Units Sold"]]) #print from row 5-12 (yes you can use the slice operator here too.), with only column "Day" and "Units Sold"
#additionally, in loc, the upper index in the slice operator is inclusive, whereas in iloc it is exclusive

print(coffee.iloc[5:13, [0, 2]]) #pretty similar to loc, this is doing the same thing as the last statement, except it only takes int values for index

#say you wanna make a correction in your data for the units sold in the second row:
coffee.loc[1, "Units Sold"] = 10
print(coffee.head(2))

#you can grab all the values of a column, like this:
print(coffee["Day"])
#if your col is a single word, you could:
print(coffee.Day)

#sorting values
print(coffee.sort_values("Units Sold")) #ascending order
print(coffee.sort_values("Units Sold", ascending = False)) #descending order

#you could get fancy with sorting, like this:
coffee.sort_values(["Units Sold", "Coffee Type"], ascending=[0,1]) #sort by descending units sold, then if they're the same, sort by coffee type ascending