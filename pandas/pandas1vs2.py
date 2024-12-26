import pandas as pd

biosnumpy = pd.read_csv('SELF-PYTHON/pandas/assets/bios.csv')
biospyarow = pd.read_csv('SELF-PYTHON/pandas/assets/bios.csv', engine='pyarrow', dtype_backend='pyarrow')

print(biosnumpy.info())
print(biospyarow.info())

#you'll see here that pandasv2 is a lot more faster bc it uses pyarrow as the backend, and it can assign a lot more specific data types, such as string and boolean,
#compared to the default backend datatypes which kind of always default to 'object'.
