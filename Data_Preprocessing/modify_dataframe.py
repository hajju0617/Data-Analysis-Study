import pandas as pd

data = {'age': [25, 30, None, 22, 35],
        'city': ['Seoul', None, 'Incheon', 'Seoul', 'Daejeon'],
        'score': [90, 85, None, 80, 92]}
df = pd.DataFrame(data)

# replace를 이용한 단일 값 변경. (Seoul -> 서울) (replace('기존값', '변경할 값'))
df['city'] = df['city'].replace('Seoul', '서울')
print('[replace를 이용한 단일 값 변경] df = \n', df)
print("*" * 30)

# replace를 이용한 여러 값 변경. (None -> 미정, Incheon -> 인천) (튜플이 아니라 딕셔너리를 이용.)
df['city'] = df['city'].replace({None: '미정', 'Incheon': '인천'})
print('[replace를 이용한 여러 값 변경] df = \n', df)
print("*" * 30)


# map을 이용한 값 변경 (key-value 형식에서 key에 있는 값을 value로 대체함.)
df2 = pd.DataFrame(data)
# map의 경우 딕셔너리를 이용해서 쓸 수도 있지만, 람다 함수를 이용할 수도 있음.
city_map = {'Seoul': '서울특별시m', None: '미정m', 'Incheon':'인천광역시m', 'Daejeon':'대전광역시m'}
df2['city'] = df2['city'].map(city_map)
print('[map을 이용한 값 변경 (딕셔너리)] df = \n', df2)
print("*" * 30)
df2['age_str'] = df2['age'].map(lambda x: f'{x}살' if pd.notna(x) else "알수없음")
print('map을 이용한 값 변경 (람다) df = \n', df2)
print("*" * 30)

# apply 함수를 이용한 값 변경.
df['age_apply'] = df['age'].apply(lambda x: x * 2 if pd.notna(x) else None)
print('[apply 함수를 이용한 값 변경] df = \n', df)
print("*" * 30)

# apply 함수를 이용한 행단위 값 변경
def age_plus_score(row):    # row에 DataFrame, 즉 df가 들어감.
    age = row['age'] if pd.notna(row['age']) else 0
    score = row['score'] if pd.notna(row['score']) else 0
    return age + score
df['age_plus_score'] = df.apply(age_plus_score, axis=1)     # axis = 1 : 행 단위 옵션.
print('[apply 함수를 이용한 행단위 값 변경] df = \n', df)
print("*" * 30)

# loc 인덱스를 이용한 값 변경
df.loc[df['score'] < 90, 'score'] = 90      # df['score'] < 90으로 90보다 작은 값을 먼저 선택 후 score컬럼만 가져와서 90으로 설정.
print('[loc를 이용한 값 변경 (90미만인 점수를 90으로 변경)] df = \n', df)
print("*" * 30)

# where 함수를 이용한 값 변경
df['age_where'] = df['age'].where(df['age'] >= 30, other = 0)   # where(값을 유지할 조건, 조건에 위배되는 것들을 변경)
print('[where 함수를 이용한 값 변경] df = \n', df)
print()
print('df["age_where"] = \n', df["age_where"])