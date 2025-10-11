import numpy as np
import pandas as pd

# 시각화 라이브러리 임포트
import matplotlib.pyplot as plt     # 파이썬의 대표적인 시각화 라이브러리
# Matplotlib은 기본적으로 영문 폰트에 최적화되어 있어서 한글을 쓰면 ??처럼 깨지거나 네모(□) 로 표시됨. 그래서 한글이 지원되는 폰트를 설정해야 한글이 정상적으로 표시됨.
plt.rc('font', family='NanumBarunGothic')
import seaborn as sns               # seaborn : matplotlib의 기능을 확장하고 고급화한 시각화 라이브러리.
import missingno as msno            # 결측치를 시각화하는데 특화 되어 있는 missingno

data = {'이름': ['김철수', '이영희', '박민수', '최지훈', '정소희'],
        '나이': [25, 30, np.nan, 22, 35],
        '도시': ['서울', None, '인천', '서울', '대전'],
        '점수': [90, 85, np.nan, 80, 92]}
df = pd.DataFrame(data)

# 결측치 히트맵.    (블랙 : 결측치가 없음, 베이지 : 결측치 존재.)
plt.figure(figsize=(8, 6))          # 8 x 6 크기의 그래프 영역 생성.
sns.heatmap(df.isnull(), cbar=False)
plt.title("결측치 히트맵")
plt.show()

# 결측치 매트릭스.  (블랙 : 결측치 없음. 화이트 : 결측치 존재.)
msno.matrix(df)
plt.title("결측치 매트릭스")
plt.show()
