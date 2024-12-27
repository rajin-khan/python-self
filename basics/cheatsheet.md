# Python Cheat Sheet

Welcome to your ultimate Python Cheat Sheet — a fun and easy guide for quick reference! Dive in and let’s make coding in Python even more enjoyable.

---

## **1. Variables**
- **Declaration**: Assign values using `=`.
```python
x = 10
y = 'hello'
z = [1, 2, 3]
```
- **Dynamic Typing**: Variables can change types.
```python
x = 10
x = 'changed!'
```
- **Naming Conventions**:
  - Use `snake_case` for variable names (e.g., `user_age`).
  - Avoid using reserved keywords (e.g., `class`, `def`, `if`).
  - Variable names should be descriptive but concise (e.g., `total_price`, not `x`).

---

## **2. Strings**
- **Manipulation**:
```python
s = 'hello world'
print(s.upper())  # HELLO WORLD
print(s.lower())  # hello world
print(s.capitalize())  # Hello world
```
- **Count Characters**:
```python
print(s.count('l'))  # 3
```
- **Concatenation & Repetition**:
```python
x = 'hi'
y = 'bye'
print(x + y)  # hibye
print(x * 3)  # hihihi
```

---

## **3. Lists**
- **Mutable**: Change values, append, extend, pop.
```python
x = [1, 2, 3]
x[0] = 'changed'
x.append(4)
x.extend([5, 6])
x.pop(1)  # Removes the second item
```
- **Copy by Reference**:
```python
y = x  # Points to the same object
y = x[:]  # Creates a new copy
```

---

## **4. Tuples**
- **Immutable**: Cannot change elements.
```python
t = (1, 2, 3)
# t[0] = 5  # Error: Tuples cannot be modified
```

---

## **5. Dictionaries**
- **Key-Value Pairs**:
```python
d = {'key1': 'value1', 'key2': 'value2'}
print(d['key1'])  # value1
d['key3'] = 'value3'
del d['key1']
```
- **Iteration**:
```python
for key, value in d.items():
    print(key, value)
```

---

## **6. Sets**
- **No Duplicates**:
```python
s = {1, 2, 3, 3}
print(s)  # {1, 2, 3}
```
- **Operations**:
```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2))  # {1, 2, 3, 4, 5}
print(s1.intersection(s2))  # {3}
print(s1.difference(s2))  # {1, 2}
```

---

## **7. Conditionals**
- **If-Else**:
```python
if x > 0:
    print('Positive')
elif x == 0:
    print('Zero')
else:
    print('Negative')
```

---

## **8. Loops**
- **For Loop**:
```python
for i in range(5):
    print(i)
```
- **While Loop**:
```python
while x < 5:
    print(x)
    x += 1
```
- **Break & Continue**:
```python
for i in range(10):
    if i == 5:
        break  # Stops the loop
    if i % 2 == 0:
        continue  # Skips to the next iteration
    print(i)
```

---

## **9. Functions**
- **Basic Syntax**:
```python
def greet(name):
    return f'Hello {name}!'
```
- **Default Parameters**:
```python
def greet(name, age=30):
    print(f'{name} is {age} years old')
```
- **Higher-Order Functions**:
```python
def apply_function(func, value):
    return func(value)
print(apply_function(lambda x: x**2, 5))  # 25
```
- **Lambda Functions**:
```python
add = lambda x, y: x + y
print(add(2, 3))  # 5
```

---

## **10. Comprehensions**
- **Lists, Dictionaries, Tuples**:
```python
squares = [x**2 for x in range(5)]
filtered = [x for x in range(10) if x % 2 == 0]
```
- **Set Comprehensions**:
```python
unique_squares = {x**2 for x in range(5)}
```
- **Generator Expressions**:
```python
lazy_squares = (x**2 for x in range(5))
```

---

## **11. Exception Handling**
- **Try-Except**:
```python
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(e)
finally:
    print('Always runs')
```

---

## **12. File I/O**
- **Read/Write**:
```python
with open('file.txt', 'w') as f:
    f.write('Hello, File!')

with open('file.txt', 'r') as f:
    print(f.read())
```

---

## **13. Advanced Concepts**
- **Unpacking**:
```python
def my_func(*args, **kwargs):
    print(args, kwargs)
my_func(1, 2, three=3, four=4)
```
- **Map & Filter**:
```python
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x*2, nums))
evens = list(filter(lambda x: x%2 == 0, nums))
```
- **Decorators**:
```python
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello")
say_hello()
```
- **Context Managers**:
```python
with open('file.txt', 'w') as f:
    f.write('Using a context manager')
```

---

## **14. F-Strings**
```python
name = 'Alice'
age = 30
print(f'{name} is {age} years old')
# With Format Specifiers
pi = 3.14159
print(f'Pi rounded to two decimals: {pi:.2f}')
```

---