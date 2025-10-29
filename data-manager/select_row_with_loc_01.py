import pandas as pd

df = pd.read_csv('C:/Data-Analysis-Study/data-manager/data/student_scores.csv')

first_row = df.loc[0]
print('== 첫 번째 레코드만 출력 ==')
print(type(first_row))
print(first_row)
print('====================')

rows = df.loc[[0, 1, 2]]        # 복수개를 ','로 선택하려면 '[](리스트)'형식으로 해야됨.
print('== 1, 2, 3번째 레코드 출력 ==')
print(rows)
print('====================')

rows_slice = df.loc[0:4]
print('== 0~4번째 레코드(총 5개) 출력 ==')
print(rows_slice)
print('====================')