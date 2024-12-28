# **Data Cleaning and Preprocessing with Pandas**

## **What is Data Cleaning and Preprocessing?**
Data cleaning involves preparing raw data for analysis by handling inconsistencies, errors, and missing values. Preprocessing transforms the data into a suitable format for machine learning, ensuring reliability and accuracy.

### **Relevance in Machine Learning**
1. **Data Integrity**: Ensures the model learns from accurate data.
2. **Feature Engineering**: Extracts meaningful features for better predictions.
3. **Automation**: Builds reusable workflows for preprocessing pipelines.

---

## **1. Handling Missing Data**
- **Detect Missing Data**:
```python
print(df.isna().sum())  # Count nulls per column
print(df.isnull().any())  # Check if any column has nulls
```
- **Fill Missing Values**:
```python
df['Column'].fillna(df['Column'].mean(), inplace=True)  # With mean
df.fillna({'Col1': 0, 'Col2': 'N/A'}, inplace=True)  # Custom values
df.interpolate(method='linear', inplace=True)  # Interpolation for numerical data
```
- **Drop Missing Values**:
```python
df.dropna(subset=['Column'], inplace=True)  # Drop rows with NaN in a column
df.dropna(axis=1, inplace=True)  # Drop columns with any NaN
```
- **Replace Placeholders**:
```python
df.replace(['N/a', 'NA', '?'], np.nan, inplace=True)
```

---

## **2. Removing Duplicates**
- **Detect Duplicates**:
```python
duplicates = df[df.duplicated()]
print(duplicates)
```
- **Drop Duplicates**:
```python
df.drop_duplicates(inplace=True)
```

---

## **3. Data Transformation**
- **Converting Data Types**:
```python
df['Column'] = df['Column'].astype('int')  # Change column to integer
pd.to_datetime(df['DateColumn'], errors='coerce')  # Convert to datetime
```
- **Renaming Columns**:
```python
df.rename(columns={'OldName': 'NewName'}, inplace=True)
```
- **String Manipulation**:
```python
df['Column'] = df['Column'].str.strip()  # Remove leading/trailing spaces
df['Column'] = df['Column'].str.replace('old', 'new', regex=True)  # Replace text
```
- **Splitting Columns**:
```python
df[['Col1', 'Col2']] = df['CombinedCol'].str.split(',', expand=True)
```

---

## **4. Feature Engineering**
- **Binning Continuous Data**:
```python
df['Category'] = pd.cut(df['Values'], bins=[0, 10, 20], labels=['Low', 'High'])
```
- **Encoding Categorical Data**:
```python
df = pd.get_dummies(df, columns=['Category'])  # One-hot encoding
df['Encoded'] = df['Category'].map({'A': 0, 'B': 1, 'C': 2})  # Manual encoding
```
- **Creating New Features**:
```python
df['Feature'] = df['Col1'] * df['Col2']
```
- **Feature Reduction**:
```python
df = df.drop(columns=['IrrelevantCol'])
```

---

## **5. Handling Outliers**
- **Detecting Outliers**:
```python
q1 = df['Column'].quantile(0.25)
q3 = df['Column'].quantile(0.75)
iqr = q3 - q1
outliers = df[(df['Column'] < q1 - 1.5 * iqr) | (df['Column'] > q3 + 1.5 * iqr)]
```
- **Capping Outliers**:
```python
df['Column'] = np.where(df['Column'] > upper_limit, upper_limit, df['Column'])
```

---

## **6. Handling Date and Time**
- **Convert to Datetime**:
```python
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
```
- **Extract Date Parts**:
```python
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
```
- **Calculate Time Differences**:
```python
df['Duration'] = (df['EndDate'] - df['StartDate']).dt.days
```

---

## **7. Integrating External Data**
- **Joining Data**:
```python
df_merged = pd.merge(df1, df2, on='Key', how='inner')  # Inner join
```
- **Appending Rows**:
```python
df_combined = pd.concat([df1, df2], axis=0)
```

---

## **8. Saving Cleaned Data**
- **Save to File**:
```python
df.to_csv('cleaned_data.csv', index=False)
df.to_excel('cleaned_data.xlsx', index=False)
```

---

## **9. Advanced Techniques**
- **Regex for Complex Cleaning**:
```python
df['Phone'] = df['Phone'].str.replace(r'[^0-9]', '', regex=True)  # Remove non-numeric chars
```
- **Conditional Transformation**:
```python
df['Category'] = np.where(df['Value'] > 10, 'High', 'Low')
```
- **Validate Data Consistency**:
```python
assert df['Column'].is_monotonic_increasing
```

---

## **10. Key Practices for ML Preprocessing**
1. **Normalize Numerical Data**:
```python
df['Normalized'] = (df['Col'] - df['Col'].mean()) / df['Col'].std()
```
2. **Handle Imbalanced Data**:
   - Oversample or undersample classes using libraries like `imbalanced-learn`.
3. **Pipeline Integration**:
   - Automate preprocessing steps with `Pipeline` in scikit-learn.

---