# **Pandas Cheat Sheet**

## **What is Pandas?**
Pandas is a powerful Python library for data analysis and manipulation. It provides:
- Data structures like **DataFrames** and **Series** for handling structured data.
- Tools for reading, transforming, analyzing, and visualizing data.

### **Relevance in Machine Learning**
- **Data Cleaning**: Handle missing values, duplicates, and inconsistencies.
- **Data Exploration**: Generate insights through statistical summaries and visualizations.
- **Feature Engineering**: Create, modify, and combine features for ML models.
- **Integration**: Prepares data for machine learning libraries like scikit-learn, TensorFlow, and PyTorch.

---

## **1. Reading Data**
- **From CSV**:
```python
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())  # View first 5 rows
```
- **From URLs**:
```python
url = 'https://example.com/data.csv'
df = pd.read_csv(url)
```
- **From Databases**:
```python
import sqlite3
conn = sqlite3.connect('database.db')
df = pd.read_sql('SELECT * FROM table_name', conn)
```
- **Other Formats**:
```python
df_excel = pd.read_excel('data.xlsx')
df_json = pd.read_json('data.json')
df_parquet = pd.read_parquet('data.parquet')
```

---

## **2. DataFrame Basics**
- **Creating DataFrames**:
```python
# From dictionaries:
data = {'A': [1, 2], 'B': [3, 4]}
df = pd.DataFrame(data)
```
- **Structure and Metadata**:
```python
print(df.shape)  # Rows x Columns
print(df.columns)  # Column names
print(df.info())  # DataFrame structure
```
- **Statistics**:
```python
print(df.describe())  # Summary stats: mean, std, etc.
```

---

## **3. Accessing Data**
- **Rows and Columns**:
```python
print(df['Column'])  # Single column
print(df[['Col1', 'Col2']])  # Multiple columns
print(df.iloc[0])  # Row by index
print(df.loc[df['Col1'] > 10])  # Rows with condition
```
- **Single Value Access**:
```python
print(df.at[1, 'Col1'])  # Fast access by label
print(df.iat[1, 0])  # Fast access by position
```
- **Iterating**:
```python
for index, row in df.iterrows():
    print(index, row['Col1'])
```

---

## **4. Modifying Data**
- **Adding Columns**:
```python
df['New Col'] = df['Col1'] * 2
```

- **Deleting Columns**:
```python
df.drop('Column Name', axis=1, inplace=True)  # Drop a single column
df.drop(['Col1', 'Col2'], axis=1, inplace=True)  # Drop multiple columns
#The axis argument in pandas specifies whether to apply the operation along rows (axis=0) or columns (axis=1). 
#For deleting columns, axis=1 is used.
```

- **Renaming**:
```python
df.rename(columns={'Old Name': 'New Name'}, inplace=True)
```
- **Handling Missing Data**:
```python
df.fillna(df.mean(), inplace=True)  # Fill with column mean
df.dropna(inplace=True)  # Drop rows with null values
```

---

## **5. Sorting and Filtering**
- **Sorting**:
```python
df.sort_values('Col1', ascending=False, inplace=True)
```
- **Filtering**:
```python
filtered = df[(df['Col1'] > 10) & (df['Col2'] == 'A')]
```

---

## **6. Grouping and Aggregation**
- **Group and Summarize**:
```python
grouped = df.groupby('Category')['Values'].sum()
```
- **Multiple Aggregations**:
```python
grouped = df.groupby('Category').agg({'Values': ['sum', 'mean'], 'Other Col': 'max'})
```
- **Pivot Tables**:
```python
pivot = df.pivot(index='Index', columns='Category', values='Values')
```

---

## **7. Merging and Concatenation**
- **Merge**:
```python
merged_df = pd.merge(df1, df2, on='Key', how='inner')
```
- **Concatenate**:
```python
concat_df = pd.concat([df1, df2])
```

---

## **8. Advanced Techniques**
- **Rank and Percent Change**:
```python
df['Rank'] = df['Values'].rank(ascending=False)
df['Pct Change'] = df['Values'].pct_change()
```
- **Apply Custom Functions**:
```python
df['New Col'] = df['Col1'].apply(lambda x: 'High' if x > 10 else 'Low')
```
- **Binning Numerical Data**:
```python
df['Bins'] = pd.cut(df['Values'], bins=[0, 10, 20, 30], labels=['Low', 'Medium', 'High'])
```

---

## **9. Null Handling**
- **Identifying Nulls**:
```python
print(df.isna().sum())  # Count nulls per column
```
- **Replacing Nulls**:
```python
df['Col1'].fillna(df['Col1'].median(), inplace=True)
```

---

## **10. Exporting Data**

- **To CSV**:
```python
df.to_csv('output.csv', index=False)
```
- **To Excel**:
```python
df.to_excel('output.xlsx', index=False)
```
- **To JSON**:
```python
df.to_json('output.json')
```
- **To Parquet**:
```python
df.to_parquet('output.parquet')
```
- **To SQL Database**:
```python
import sqlite3
conn = sqlite3.connect('output.db')
df.to_sql('table_name', conn, if_exists='replace', index=False)
```
---

## **11. Best Practices in ML with Pandas**
1. **Efficient Data Loading**:
   - Use Parquet for faster reads/writes compared to CSV.
   - Leverage PyArrow backend for better type handling (e.g., strings, booleans).
2. **Data Cleaning**:
   - Handle missing values effectively (e.g., imputation).
   - Remove duplicate rows: `df.drop_duplicates(inplace=True)`.
3. **Feature Engineering**:
   - Create new features using `.apply()` or vectorized operations.
   - Encode categorical variables with `.get_dummies()` or `pd.Categorical`.
4. **Binning and Categorization**:
   - Use `.cut()` or `.qcut()` for numerical binning to create categorical features.

---