import pandas as pd


data = {
    'student_id': ['S001', 'S002', 'S003', 'S004', 'S005'],
    'name':       ['김민수', '이수진', '박지훈', '최윤아', '정현우'],
    'gender':     ['M', 'F', 'M', 'F', None],
    'math':       [88, 79, None, 84, 77],
    'english':    [92, 85, 87, None, 75],
    'korean':     [90, 84, 86, 85, 79]
}
df = pd.DataFrame(data)

print("=== 데이터 구조 요약 ===")
print(df.info())

print("=== 데이터 통계 요약 ===")
print(df.describe())

print("=== 결측값 확인 ===")
print(df.isnull())

print("=== 열별 결측값 개수 ===")
print(df.isnull().sum())

print("=== 성별 분포 확인 ===")
print(df['gender'].value_counts())

print("=== 비율로 보기 ===")
print(df['gender'].value_counts(normalize=True))