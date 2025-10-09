import pandas as pd
import numpy as np

'''
pandas의 자료들은 numpy 라는 라이브러리를 통해서 
numpy Array 형태로 저장 되어 있음.

데이터 측정을 할 때 어떤 속성의 데이터를 살펴볼 건지 결정하는 단계가 있는데
그때 numpy의 특정 객체들만 살펴보기 위해 'import numpy' 했음.
'''


data = {
    'name': ['김민수', '이지영', '박준호', '최서연', '정도윤'],
    'age': [25, 30, 28, 22, 35],
    'city': ['서울', '부산', '인천', '서울', '대전'],
    'score': [90, 85, 95, 80, np.nan]   # np.nan : numpy 상수. (결측치)
}

df = pd.DataFrame(data)
print('df = \n', df)
print()

# 데이터 측정.
print('df.describe() = \n', df.describe())  # describe() : 숫자형 데이터만 요약.
print()

# 모든 데이터 타입 측정.
print("df.describe(include = 'all')\n", df.describe(include='all'))
print()

# 수치형 데이터 측정.
print('df.describe(include = [np.number]) = \n', df.describe(include=[np.number]))  # 25행과 동일한 결과.
print()

# 범주형 데이터 측정.
print('df.describe(include = ["object"]) = \n', df.describe(include=['object']))
print()

# 특정 열 분석.
print('df["score"].describe() = \n', df["score"].describe())