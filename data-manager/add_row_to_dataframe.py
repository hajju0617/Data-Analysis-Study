import pandas as pd

df = pd.read_csv('C:/Data-Analysis-Study/data-manager/data/student_scores.csv')

new_student = pd.DataFrame([{
    'student_id': 'S031',
    'name': '강지민',
    'gender': 'F',
    'grade': 1,
    'class': 1,
    'math': 89,
    'english': 91,
    'science': 87,
    'korean': 90,
    'average': (89 + 91 + 87 + 90) / 4
}])

# ignore_index=True : 새로운 인덱스를 매김.
df = pd.concat([df, new_student], ignore_index=True)
# loc : 인덱스 이름, iloc : 순서.
print(df)
print(df.loc[30])
print(df.iloc[30])
print()

tmp = {
    'Name': ['김민수', '이수진', '박지훈'],
    'score': [88, 92, 85]
}
df2 = pd.DataFrame(tmp)
print(df2)
df2.index = [100, 101, 102]
print(df2)
print(df2.iloc[1])
print('==========')
# print(df2.loc[1])     # 에러 발생. (iloc[1] -> 순서상 2번째 행이므로 '이수진'이 출력됨. 하지만 loc[1] -> 라벨이 '1'인 행이 없으므로 에러 발생.)
