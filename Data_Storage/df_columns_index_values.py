import pandas as pd

data = {
    "이름": ["김철수", "이영희", "박민수", "최지훈", "정소희"],
    "학년": [1, 2, 3, 4, 2],
    "학점": [4.2, 3.8, 4.5, 3.9, 3.5],
    "학과": ["컴퓨터학", "경영학", "농학", "교육학", "영어영문학"],
    "동아리": ["프로그래밍", "독서토론", "로봇공학", "봉사활동", "음악감상"]
}

# DataFrame 객체 생성.
df = pd.DataFrame(data)
print('df = \n', df)
print()

# DataFrame 인덱스.
print('index: ', df.index)

# DataFrame 컬럼.
print('column: ', df.columns)

# DataFrame 행.
print('nrows_py_list: ', df.values.tolist())        # values.tolist() : 파이썬 리스트 형태.
print('nrows_NumPy_array: ', df.values)             # values : NumPy 배열 형태.

# DataFrame 값.
print('nvalues: ', df.values.flatten())         # flatten() : DataFrame의 모든 값을 1차원 배열로 변환.