import pandas as pd

df = pd.read_csv('C:/Data-Analysis-Study/data-manager/data/student_scores.csv')

english_rows = df.loc[df['english'] > 90, 'english']
print('== 90보다 높은 영어점수 ==')
print(english_rows)
print('====================')

english_and_math = df.loc[(df['english'] > 90) & (df['math'] > 90)]
print('== 영어, 수학이 90보다 높음 ==')
print(english_and_math)