import pandas as pd
import numpy as np

점수_데이터 = [72, 68, 75, 282, 64, 31, 78, 69, 88, 92, 22, 84, 61, -90, 130, 66]
학번_데이터 = list(range(1001, 1001 + len(점수_데이터)))

df = pd.DataFrame({
    '학번': 학번_데이터,
    '점수': 점수_데이터
})

# Z-점수 계산.
score_mean = df['점수'].mean()      # 점수의 평균.
score_std = df['점수'].std()        # 점수의 표준편차.
df['score_z'] = (df['점수'] - score_mean) / score_std
print('df = \n', df)
print("*" * 30)

# 임계값 설정 및 이상치 여부 판단.
threshold = 2                       # 임계값.
df['is_outlier'] = df['score_z'].abs() > threshold
print('df = \n', df)
print("*" * 30)

# 이상치 데이터 출력.
print('df[df["is_outlier"]] = \n', df[df["is_outlier"]])    # df["is_outlier"] 이 값 자체가 boolean 값들 이기 때문에 True인 값만 출력.
print("*" * 30)

# 이상치 비율 출력.
print('df["is_outlier"] = \n', df['is_outlier'])
print('df["is_outlier"].mean() = \n', df['is_outlier'].mean())  # True = 1, False = 0으로 취급되므로 True의 비율을 구하고.
print('df["is_outlier"].mean() * 100 = \n', df['is_outlier'].mean() * 100)  # * 100 해주면 비율이 나옴.