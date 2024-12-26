import pandas as pd

df = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9]], columns = ["A", "B", "C"]) #load up some data into the dataframe

print(df.head(5)) #print the first 5 rows
print(df.tail(2)) #print the last 2 rows

print(df.columns) #see just the cols
print(df.index) #see the indexes

print(df.info()) #to see info about the dataframe

print(df.describe()) #returns statistical info like count, mean, standard dev, min, q1, q2, q3, max

print(df.shape) #shows the shape of the dataframe (r x c)