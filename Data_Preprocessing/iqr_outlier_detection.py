import pandas as pd
import numpy as np

점수_데이터 = [72, 68, 75, 282, 64, 31, 78, 69, 88, 92, 22, 84, 61, -90, 130, 66]
학번_데이터 = list(range(1001, 1001 + len(점수_데이터)))

df = pd.DataFrame({
    '학번': 학번_데이터,
    '점수': 점수_데이터
})

# 사분위 범위 경계값 계산.
q1 = df['점수'].quantile(0.25)      # 데이터의 25% 지점.
q3 = df['점수'].quantile(0.75)      # 데이터의 75% 지점.

iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr        # 하한값.
upper_bound = q3 + 1.5 * iqr        # 상한값.


# IQR 통계량 출력
print(f'q1 = {q1}')
print(f'q3 = {q3}')
print(f'iqr = {iqr}')
print(f'lower_bound = {lower_bound}')   # 30.625
print(f'upper_bound = {upper_bound}')   # 117.625
# 즉, 30.625 이하인 값, 117.625 이상인 값은 이상치로 간주.