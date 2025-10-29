import pandas as pd

df = pd.read_csv('C:/Data-Analysis-Study/data-manager/data/student_scores.csv')
name = df['name']
# print(name)
print(type(name))
print(name.head())