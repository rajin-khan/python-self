import pandas as pd

coffee = pd.read_csv('SELF-PYTHON/pandas/assets/coffee_new.csv')

#say you wanted to see how one day's revenue was doing compared to the previous, you could use the shift method.

#adding a new row called 'yesterday_revenue'
coffee['yesterday_revenue'] = coffee['revenue'].shift(2) #normally, we'd do shift(1), but shift(2) bc we have 2 types of coffee being sold each day
#so, we see the diff between one row and the next for the specified col, or in this case, the diff between 2 rows and the next 2 rows.

print(coffee)

#maybe then, we could calculate the % increase between the prev day and the next day.
coffee['pct_change'] = (coffee['revenue']/coffee['yesterday_revenue'])*100
print(coffee)

bios = pd.read_csv('SELF-PYTHON/pandas/assets/bios.csv')
#if we wanted to, say rank athletes based on their height, there's a built in function for that.
bios['height_rank'] = bios['height_cm'].rank(ascending=False)
print(bios[['name', 'height_rank']])

#or, the cumulative sum function:
coffee['cumulative_revenue'] = coffee['revenue'].cumsum()

#you can always use chatgpt to generate data for specific purposes.