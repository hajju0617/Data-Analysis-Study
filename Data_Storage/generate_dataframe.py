import pandas as pd
import os
os.chdir("c:/Data-Analysis-Study/Data_Storage/data")

data = {
    "이름": ["김철수", "이영희", "박민수", "최지훈", "정소희"],
    "학년": [1, 2, 3, 4, 2],
    "학점": [4.2, 3.8, 4.5, 3.9, 3.5],
    "학과": ["컴퓨터공학", "경영학", "전자공학", "의학", "심리학"],
    "동아리": ["프로그래밍", "독서토론", "로봇공학", "봉사활동", "음악감상"]
}

# dictionary -> (변환) DataFrame 생성.
df_dict = pd.DataFrame.from_dict(data)

# csv -> (변환) DataFrame 생성.
df_csv = pd.read_csv('students.csv')

# json -> (변환) DataFrame 생성.
df_json = pd.read_json('students.json')

# 세 가지 비교
print('df_dict.shape:', df_dict.shape)
print('df_csv.shape:', df_csv.shape)
print('df_json.shape:', df_json.shape)
print()
print('df_dict: ', df_dict)
print('df_csv: ', df_csv)
print('df_json: ', df_json)