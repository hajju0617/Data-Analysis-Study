import pandas as pd


students = pd.DataFrame({
    'student_id': ['S001', 'S002', 'S003', 'S004'],
    'name': ['김민수', '이수진', '박지훈', '최윤아']
})


scores = pd.DataFrame({
    'student_id': ['S001', 'S002', 'S005'],
    'math': [88, 79, 90],
    'english': [92, 85, 94]
})

# how='inner' : INNER JOIN
merged = pd.merge(students, scores, how='inner', on='student_id')
print(merged)
print('=====left join=====')
merged = pd.merge(students, scores, how='left', on='student_id')
print(merged)
print('=====rigth join=====')
merged = pd.merge(students, scores, how='right', on='student_id')
print(merged)
print('=====outer join (SQL에선 FULL OUTER JOIN)=====')
merged = pd.merge(students, scores, how='outer', on='student_id')
print(merged)
print('==========')