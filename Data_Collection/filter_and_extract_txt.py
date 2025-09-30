import re # 정규 표현식(regular expression, regex)을 다루는 내장 모듈.
import os
os.chdir('C:/Data-Analysis/Data_Collection/data')

with open('callcenter20250301.log', 'r', encoding='utf-8') as txt_file:
    content = txt_file.read()
pattern = re.compile(r'(\d{6})-(\d{7})')    # ()를 이용해서 그룹화. 생년월일 : 1그룹, 뒷자리 : 2그룹.
print(pattern)
# r'...' : raw string 표시. 정규식 표현을 그대로 쓰기 위함.
masked_content = pattern.sub(r'\1-*******', content)    # \1 : 1그룹, ******* : 2그룹을 뜻함.

with open('callcenter20250301_masked.log', 'w', encoding='utf-8') as masked_txt_file:
    masked_txt_file.write(masked_content)
print('주민등록번호 뒷자리 마스킹 완료. "callcenter20250301_masked.log.txt" 파일로 저장되었음.')

