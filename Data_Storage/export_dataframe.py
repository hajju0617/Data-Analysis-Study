import pandas as pd
import os
os.chdir('C:/Data-Analysis-Study/Data_Storage/data')

data = {
    "이름": ["김철수", "이영희", "박민수", "최지훈", "정소희"],
    "학년": [1, 2, 3, 4, 2],
    "학점": [4.2, 3.8, 4.5, 3.9, 3.5],
    "학과": ["컴퓨터공학", "경영학", "전자공학", "의학", "심리학"],
    "동아리": ["프로그래밍", "독서토론", "로봇공학", "봉사활동", "음악감상"]
}

# DataFrame 객체 생성.
df = pd.DataFrame(data)

# CSV, JSON 형식으로 저장.
df.to_csv('students_scores.csv', encoding='utf-8', index=False)
df.to_json('students_scores.json', force_ascii=False, orient='records', indent=4)

# HTML 형식으로 저장.
html_table = df.to_html()           # DataFrame -> HTML 변환.
print('html_table: \n', html_table)

with open('students_scores.html', 'w', encoding='utf-8') as html_file:
    html_file.write(html_table)