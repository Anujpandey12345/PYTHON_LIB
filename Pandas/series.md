# 📊 Pandas Series Guide

## What is a Pandas Series?

A **Series** is a one-dimensional labeled array capable of holding any data type (integers, strings, floats, Python objects, etc.). The axis labels are collectively called the **index**.

---

## 🚀 Getting Started

### Installation

First, you need to install the required libraries:

```bash
pip install pandas
pip install numpy
```

> **Note:** NumPy is only required if you're working with arrays.

### Importing Libraries

```python
import pandas as pd
import numpy as np  # Only if using arrays
```

---

## 💻 Creating a Series

Below is a comprehensive example showing different ways to create a Pandas Series from various data structures.

### Complete Example Code

```python
import pandas as pd
import numpy as np

# Step 1: Create different data types and items
labels = ['a', 'b', 'c', 'd', 'e']
arr = np.array([10, 20, 30, 40, 50])
my_list = [30, 40, 50, 60, 70]
my_dict = {1: 20, 2: 30, 3: 40, 4: 90, 5: 100}  # Keys are numbers
my_dictC = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}  # Keys are characters

# Step 2: Create Series from different data structures

# From NumPy array
print(pd.Series(arr))

# From Python list
print(pd.Series(my_list))

# From list with custom labels
print(pd.Series(my_list, index=labels))

# From list with different custom labels
print(pd.Series(my_list, index=['o', 'q', 'a', 'h', 'f']))

# From dictionary (numeric keys)
print(pd.Series(my_dict))
# Note: Dictionary keys automatically become the index labels

# From dictionary (character keys)
print(pd.Series(my_dictC))
# Note: Character keys are used as index labels
```

---

## 🔑 Key Points

- **Custom Index:** You can specify custom index labels using the `index` parameter
- **Dictionary Keys:** When creating a Series from a dictionary, the keys automatically become the index labels
- **Flexibility:** Series can hold any data type and can be created from various Python data structures

---

## 📚 Summary

| Data Source | Syntax | Index |
|-------------|--------|-------|
| NumPy Array | `pd.Series(arr)` | Default (0, 1, 2, ...) |
| Python List | `pd.Series(my_list)` | Default (0, 1, 2, ...) |
| List + Custom Index | `pd.Series(my_list, index=labels)` | Custom labels |
| Dictionary | `pd.Series(my_dict)` | Dictionary keys |

---

**Happy Learning! 🎉**