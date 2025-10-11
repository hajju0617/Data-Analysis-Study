import pandas as pd
import numpy as np

data = {'이름': ['김철수', '이영희', '박민수', '최지훈', '정소희'],
        '나이': [25, 30, np.nan, 22, 35],
        '도시': ['서울', None, '인천', '서울', '대전'],
        '점수': [90, 85, np.nan, 80, 92]}

df = pd.DataFrame(data)

# 결측치 여부 확인. (isnull(), isna() : 둘 다 동일한 기능. 결측치 일 경우 True)
print('df.isnull() = \n', df.isnull())
print('*' * 20)
print(f'df.isna() = \n {df.isna()}')
print("=" * 30)

# 열별, 행별 결측치 개수 확인.
print('[열별] df.isnull().sum() = \n', df.isnull().sum())  # sum() : True(결측치)의 개수를 세어줌.
print('*' * 20)
print(df)
print('[행별] df.isnull.sum(axis = 1) = \n', df.isnull().sum(axis =  1))   # axis = 1 : (가로 방향)행별 결측치.
print("=" * 30)

# 특정 열, 행 결측치 확인.
print('[행 결측치] df[df.isnull().any(axis =1)] = \n', df[df.isnull().any(axis=1)])     # any()를 이용해서 1개 이상의 결측치가 있을 경우 추출.
print('*' * 20)
print('[열(나이) 결측치]df[df["나이"].isnull()] = \n', df[df["나이"].isnull()])
print("=" * 30)

# 결측치가 아닌 항목 확인.
print('df.notnull() = \n', df.notnull())
print("=" * 30)

# 결측치 비율 확인.
# df.isnull().sum() : 특정 열별 결측치의 개수. // df.isnull().sum().sum() : 그 개수의 총합.
print('[결측치 비율 확인] df.isnull().sum().sum() / (df.shape[0] * df.shape[1]) * 100 = \n', df.isnull().sum().sum() / (df.shape[0] * df.shape[1]) * 100)
print('df.shape[0] = \n', df.shape[0])  # DataFrame 행의 개수.
print('df.shape[1] = \n', df.shape[1])  # DataFrame 열의 개수.
