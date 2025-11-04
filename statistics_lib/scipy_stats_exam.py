from scipy import stats

'''
norm : 정규 분포(Normal Distribution)를 나타내는 객체.
pdf() : 확률 밀도 함수 (Probability Density Function).
'''
pdf_value = stats.norm.pdf(1)
print(pdf_value)