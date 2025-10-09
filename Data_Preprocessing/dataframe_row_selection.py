import pandas as pd

data = {
    "이름": ["김철수", "이영희", "박민수", "최지훈", "정소희"],
    "학년": [1, 2, 3, 4, 2],
    "학점": [4.2, 3.8, 4.5, 3.9, 3.5],
    "학과": ["컴퓨터공학", "경영학", "전자공학", "의학", "심리학"],
    "동아리": ["프로그래밍", "독서토론", "로봇공학", "봉사활동", "음악감상"]
}

df = pd.DataFrame(data)
print('df = \n', df)
print()

# DataFrame 인덱스 지정.
df = df.set_index('이름')   # 다룰 데이터의 중요한 속성을 인덱스로 설정함으로서 탐색이 편리해지고 좀 더 직관적으로 이해할 수 있음.
print('df = \n', df)
print()

# DataFrame 행 선택.
print('df.loc["김철수"] = \n', df.loc['김철수'])
print()
print('df.loc[["김철수", "이영희"]] = \n', df.loc[['김철수', '이영희']])    # 리스트로 전달.
print()
print('df.loc["김철수":"최지훈"] = \n', df.loc['김철수':'최지훈'])
print()

# DataFrame 위치 기반 행 선택.  (인덱스 기준)
print('df.iloc[0] = \n', df.iloc[0])
print()
print('df.iloc[1] = \n', df.iloc[1])
print()
print('df.iloc[[0, 1]] = \n', df.iloc[[0, 1]])  # 리스트로 전달해야 됨.
print()
print('df.iloc[0:2] = \n', df.iloc[0:3])
print()

# DataFrame 조건 기반 선택. (전달할 리스트의 요소는 DataFrame의 레코드의 수와 동일해야됨.)
print('df.loc[[True, True, False, False, True]] = \n', df.loc[[True, True, False, False, True]])
print()

print('df["학점"] = \n', df["학점"])
print('df["학점"] >= 4.0 = \n', df['학점'] >= 4.0)
print('df.loc[df["학점"] >= 4.0] = \n', df.loc[df["학점"] >= 4.0])
print()
print('df[["학점", "학년"]] = \n', df[["학점", "학년"]])
print('df[df["학년"] == 2] = \n', df[df["학년"] == 2])
print('df[(df["학년"] == 2) & (df["학점"] >= 3.7)] = \n', df[(df["학년"] == 2) & (df["학점"] >= 3.7)])
