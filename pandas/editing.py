import pandas as pd

df = pd.read_csv('SELF-PYTHON/pandas/assets/pokemon_data.csv')

#say we wanna add a new column, called Total, of all the numeric stats
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
#the new col, total, is taken and added to the end as a col. we can print to verify.
print(df)
#always better to check and verify.
#in some cases, certain software (not VSC), like Jupyter Notebooks, may same the previous dataframe (with the totals col) even if you comment it out.
#in that case, or otherwise:
df = df.drop(columns=['Total']) #we have to save the dataframe to the new one, because it doesn't directly modify the original df unless you assign it.
print(df)

#an easier way to add might have been:
df['Total'] = df.iloc[:, 4:10].sum(axis=1) #so for all rows, take col 4-9 (10 means not including 10), add along the horizontal axis (1 = hor, 0 = vert)

#say we wanna save the col in a specific place, not at the far right end of the table:
#df = df[['Total', 'HP', 'Attack']] 
#.. and we'd continue adding the name of all the rows in the order we want, and saving it in the og dataframe

#but that can be tedious, so we can just save the name of all the cols in a list like this:
cols = list(df.columns.values)
df = df[cols[0:4], 'Total' + [cols[-1]] + cols[4:12]] #[cols[-1]] is surrounded by another bracket because this format accepts a list only, cols[-1] returns only a string, so we wrap it in a list bracket.
print(df) 
# -1 in the index of cols simply means the last index. cols[10] would have achieved the same result.

#ALL OF THE CHANGES YOU'RE MAKING HERE ARE NOT ACTUALLY CHANGING YOUR CSV FILE.
