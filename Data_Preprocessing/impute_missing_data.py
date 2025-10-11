import pandas as pd
import numpy as np
import os
os.chdir('C:/Data-Analysis-Study/Data_Preprocessing/data')

file = "raw_large_shopping_customer.csv"
df = pd.read_csv(file)  
print(df.isnull().sum())        # 결측치의 개수.

# df.shape[1] : 컬럼의 개수. (컬럼의 개수가 5개이므로 4개 이상의 값이 채워져 있는 것만 남김.)
df_cleaned = df.dropna(thresh=df.shape[1] - 1)
print('df_cleaned = \n', df_cleaned)
print('*' * 30)

# 나이, 소득의 결측치를 평균값 대치 및 결과 출력.
df_cleaned.loc[:, ['나이', '소득']] = df_cleaned[['나이', '소득']].fillna(df_cleaned[['나이', '소득']].mean())
print('df_cleaned = \n', df_cleaned)
print('*' * 30)

# 지출, 평균구매횟수의 결측치를 선형보간법 적용
df_cleaned.loc[:, ['지출', '평균구매횟수']] = df_cleaned[['지출', '평균구매횟수']].interpolate(method='linear')     # interpolate(method='linear') : 해당 열의 다른 데이터 값 사이의 관계를 이용해 결측치를 추정함.
print('df_cleaned = \n', df_cleaned)
print('*' * 30)

# csv 파일로 저장
df_cleaned.to_csv("cleaned_large_shopping_customer.csv", index=False, encoding="utf-8-sig")