import pandas as pd

df = pd.read_csv('C:/Data-Analysis-Study/data-manager/data/student_scores.csv')

print(df.head())
df['height'] = 0
print(df.head())
df['avg_kor_eng_math'] = (df['math'] + df['english'] + df['korean']) / 3
print(df.head())