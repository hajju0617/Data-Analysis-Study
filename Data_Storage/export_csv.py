import pandas as pd
import os
os.chdir('C:/Data-Analysis/Data_Storage/data')

data = {
    'student_id': [101, 102, 103, 104, 105],
    'database_score': [85, 76, 92, 63, 88],
    'cloudcomputing_score': [78, 82, 95, 70, 84],
    'python_score': [92, 78, 85, 75, 91],
    'watch_rate': [0.95, 0.87, 0.99, 0.80, 0.93]
}

# data를 이용해서 DataFrame 생성.
df = pd.DataFrame(data)
print('df = \n', df)

# CSV 형식으로 저장.
df.to_csv('student_analysis.csv', encoding='utf-8', index=False)