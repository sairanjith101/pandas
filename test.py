import pandas as pd

data = {
    'name': ['sai', 'ajith', 'siva'],
    'age': [20, 30, 40],
    'salary': [10000, 20000, 30000]
}

df = pd.DataFrame(data, index=[1, 2, 3])
print(df)