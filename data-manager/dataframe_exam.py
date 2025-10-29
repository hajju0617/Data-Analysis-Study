import pandas as pd

data = {
    'Name': ['John Doe', 'Jane Doe'],
    'Age': [23, 28],
    'Country': ['USA', 'Canada']
}
df = pd.DataFrame(data)
print(df)