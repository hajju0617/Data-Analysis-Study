import pandas as pd

df = pd.read_csv('C:/Data-Analysis-Study/data-manager/data/student_scores.csv')

first_row = df.iloc[0]
print('== 첫 번째 행 선택 ==')
print(type(first_row))
print(first_row)
print('====================')

rows = df.iloc[[0, 1, 2]]
print('== 0, 1, 2 행 선택 ==')
print(type(rows))
print(rows)
print('====================')

rows_slice = df.iloc[0:4]
print('== 0~(4-1)행(총 4행) 선택 ==')
print(rows_slice)
print('====================')

selected_data = df.iloc[0:3, 0:3]
print('== 0~(3-1)행 (총3행) 선택 & 0~(3-1)번째 열 선택')
print(selected_data)