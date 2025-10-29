import pandas as pd

df = pd.read_csv('C:/Data-Analysis-Study/data-manager/data/student_scores.csv')

english = df.loc[:, 'english']
print('== english 열만, 0~29행까지')
print(english)
print('====================')

row_english = df.loc[0, 'english']
print('== english 열만, 0행 ==')
print(row_english)
print('====================')

rows_english = df.loc[0:2, 'english']
print('== english 열만, 0~2행 ==')
print(rows_english)
print('====================')