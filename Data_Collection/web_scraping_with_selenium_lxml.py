'''
코랩일 경우 아래 코드가 필요함.
1. Chrome 브라우저를 리눅스 서버에 다운로드
2. 다운로드한 패키지를 리눅스 시스템에 설치
3. 리눅스 시스템의 Chrome 실행 파일 경로를 지정
'''
# !curl -o google-chrome-stable_current_amd64.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# !apt install ./google-chrome-stable_current_amd64.deb -y
# !pip install selenium webdriver_manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from lxml import html
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')               # 브라우저 창 없이 실행
# chrome_options.add_argument('--no-sandbox')             # 보안모드 비활성화 (Colab 필수)
# chrome_options.add_argument('--disable-dev-shm-usage')  # 메모리 부족 방지 (Colab 필수)
chrome_options.add_argument('--window-size=1920x1080')  # 창 크기 설정(가상)
# chrome_options.add_argument('--disable-gpu')            # GPU 가속 비활성화 (일부 환경 안정성)
# chrome_options.binary_location = "/usr/bin/google-chrome-stable"  # Colab용 크롬 경로 지정

# 드라이버 실행
driver = webdriver.Chrome(options=chrome_options)



# 사이트 접속
url = 'https://www.naver.com/'
driver.get(url)

# 사이트 접속 대기
time.sleep(2)

# 페이지 제목 출력.
page_source = driver.page_source
tree = html.fromstring(page_source)

try:
    title_text = tree.xpath('//title/text()')
    print('웹 페이지 제목 (xpath) : ', title_text[0] if title_text else '제목 없음')
except Exception as e:
    print(f'xpath 추출 실패 : {e}')

# 드라이버 종료.
driver.quit()
