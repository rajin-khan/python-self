# **NumPy Cheat Sheet**

## **What is NumPy?**
NumPy (Numerical Python) is a fundamental library for numerical and scientific computing in Python. It provides:
- High-performance arrays and matrix operations.
- Efficient numerical computations (e.g., linear algebra, statistics).
- A foundation for other machine learning libraries like TensorFlow, PyTorch, and scikit-learn.

### **Relevance in Machine Learning**
- **Data Preparation**: Data manipulation, cleaning, and transformation.
- **Linear Algebra**: Essential for understanding ML concepts like gradient descent, matrix factorization, etc.
- **Statistics**: Compute means, standard deviations, and other statistics.
- **Efficiency**: Highly optimized for performance-critical tasks.

---

## **1. Creating Arrays**
- **From Lists**:
```python
import numpy as np
arr = np.array([1, 2, 3])  # 1D array
print(arr)
```
- **From Ranges**:
```python
arr = np.arange(10, 20, 2)  # Start, Stop, Step
print(arr)
```
- **Special Arrays**:
```python
zeros = np.zeros((3, 3))  # 3x3 matrix of zeros
ones = np.ones((2, 4))  # 2x4 matrix of ones
identity = np.identity(4)  # 4x4 identity matrix
random = np.random.rand(3, 3)  # 3x3 random floats
```

---

## **2. Accessing and Modifying Data**
- **Indexing and Slicing**:
```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a[1, 2])  # Access element at row 1, column 2
print(a[:, 1])  # Access all rows, column 1
```
- **Boolean Masking**:
```python
filedata = np.array([[1, 2, 3], [4, 5, 6]])
print(filedata[filedata > 3])  # [4, 5, 6]
```
- **np.where()**:
```python
arr = np.array([[1, 2], [3, 4]])
result = np.where(arr % 2 == 0, 0, arr)  # Replace evens with 0
```

---

## **3. Reshaping and Reorganizing**
- **Reshape**:
```python
arr = np.arange(10, 26)
newarr = arr.reshape((4, 4))  # 4x4 matrix
```
- **Stacking**:
```python
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
stacked = np.vstack([v1, v2])  # Vertical stack
```

---

## **4. Mathematics with Arrays**
- **Basic Operations**:
```python
a = np.array([1, 2, 3])
print(a + 2)  # [3, 4, 5]
print(a ** 2)  # [1, 4, 9]
```
- **Linear Algebra**:
```python
a = np.ones((2, 3))
b = np.full((3, 2), 2)
print(np.matmul(a, b))  # Matrix multiplication
```
- **Statistics**:
```python
stats = np.array([[1, 2], [3, 4]])
print(np.mean(stats))  # Mean
print(np.min(stats, axis=0))  # Column-wise min
```

---

## **5. Image Manipulation**
- NumPy arrays store pixel data for images:
```python
image = np.array([[[255, 0, 0], [0, 255, 0]], [[0, 0, 255], [255, 255, 0]]])
```
- Modify image colors using `np.where`:
```python
updated_image = np.where(image == 0, 255, image)  # Replace black with white
```

---

## **6. Limitations**
- **Type Coercion**:
  Arrays must contain elements of the same type. Mixed types are converted:
```python
arr = np.array([[1, 2], [3, "hello"]])
print(arr)  # All elements become strings
```

---

## **7. File Operations**
- **Load/Save Data**:
```python
filedata = np.genfromtxt('file.txt', delimiter=',')
np.savetxt('output.txt', filedata, delimiter=',')
```

---

## **8. Best Practices in ML with NumPy**
1. **Efficient Preprocessing**: Use slicing, masking, and vectorized operations to preprocess data.
2. **Avoid Pointer Issues**: Always `.copy()` arrays when needed:
```python
b = a.copy()
```
3. **Integrate with ML Libraries**: Use NumPy arrays to prepare data for scikit-learn, TensorFlow, etc.

---