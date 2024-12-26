import pandas as pd

coffee = pd.read_csv('SELF-PYTHON/pandas/assets/coffee.csv')

coffee['price'] = 4.99 #adds this col to the end of the dataframe array
print(coffee.head())

#we may add diff cols, perhaps with the use of a numpy "helper method".
import numpy as np

coffee['new_price'] = np.where(coffee['Coffee Type']=='Espresso', 3.99, 5.99) #you already know how where in numpy works works
print(coffee.drop(columns=['price'])) #now, in this session, adding a new col stays permanenetly, but dropping doesn't.

#what this means is, if you did coffee.drop(a column) in one line, and printed the dataframe coffee in the next line, it wouldn't show the dropped col.
#but you added a col, and then printed the df coffee in the next line separately, it would show it.
#in order to achieve the same effect as adding a col, whereby one line drops it persistently for this session, we can:
coffee.drop(columns=['price'], inplace=True)
#or, coffee = coffee.drop(columns=['price'])
print(coffee)

#dataframes in panda have the same pointer issue as lists in python, and numpy.
#if create a copy of the df coffee like this:
coffee_new = coffee
#and then we make modifications to the coffee_new df, but print the coffee df, the same changes are shown there. this is because pandas,
#in the above statements, just creates a pointer to coffee. so, we instead do:
coffee_new = coffee.copy
#and this creates a true copy of that coffee df in the coffee_new df.

#let's rename new_price to price:
coffee.rename(columns={'new_price':'price'}, inplace=True) #we pass in a dictionary, and if the col is 'new_price', we replace it with 'price'

coffee['revenue'] = coffee['Units Sold'] * coffee['price'] #you can multiply and combine cols like this
print(coffee)


#trying some more fancy stuff where we add new columns based on filtered results:
bios = pd.read_csv('SELF-PYTHON/pandas/assets/bios.csv')

bios['first name'] = bios['name'].str.split(' ').str[0] #coverting the name to string, splitting it using a delimiter of space, then taking the first element from the separated elements.

#add more fancy cols:
bios['born_datetime'] = pd.to_datetime(bios['born_date']) #converts the born_date column to a datetime datatype and stores it in a new col.
#now we can split the datetime data into year, months and stuff
bios['born_year'] = bios['born_datetime'].dt.year #kinda like .str, there is a .dt for datetime datatypes too.

print(bios[['name', 'born_year']]) #view the info you just saved.

#even fancier stuff (although this is not optimized for pandas, using regex and local pandas methods are better):

#the apply keyword allows you to put any function in the place after.
bios['height_category'] = bios['height_cm'].apply(lambda x: 'Short' if x<165 else ('Average' if x<185 else 'Tall')) #you know how lambda functions work
#what this is doing is assigning values to the height category col, so if height_cm values is less than 165, height_category gets assigned 'Short'
print(bios[['name', 'height_cm', 'height_category']])

#as the apply keyword allows you to put in any function, you could also define a function separately, then apply it, for example:
def categorize_athletes(row):
    if row['height_cm'] <175 or row['weight_kg'] <70:
        return 'Lightweight'
    elif row['height_cm'] <185 or row['weight_kg'] <80:
        return 'Middleweight'
    else:
        return 'Heavyweight'

bios['Overall Category'] = bios.apply(categorize_athletes, axis=1) #we need to specify that this is happening on rows, so axis = 1
print(bios.head())


#NONE OF THESE MODIFY THE ORIGINAL FILE, IT IS ONLY THIS DATAFRAME INSTANCE.
#to save this one, we can just:
bios.to_csv('SELF-PYTHON/pandas/assets/bios_new.csv', index=False) #index=False bc otherwise it save the index as a separate col with values from 0 and so on.
#ofc you can save it in tons of other formats