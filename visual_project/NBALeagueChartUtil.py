# 시간에 대한 라이브러리 import
import time
# pandas 라이브러리 import
import pandas as pd

# bs4 라이브러리에 포함된 BeautifulSoup import
from bs4 import BeautifulSoup
# selenium 라이이브러리에 포함된 webdriver import
from selenium import webdriver


# class 생성`
class NBARanking():
    # encoding 타입
    myencoding = 'utf-8'

    # class 생성자 method
    def __init__(self, chartname, url):
        self.soup = None
        self.chartname = chartname
        self.url = url
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)

    # 크롤링으로 데이터 가져오는 method
    def getWebDriver(self):
        wait = 10
        time.sleep(wait)
        mypage = self.driver.page_source
        return BeautifulSoup(mypage, 'html.parser')

    # 파일 저장 method
    def save2Csv(self, result):
        # 컬럼명 리스트로 저장
        mycolumn = ['Team', 'Games Played', 'Wins', 'Losses', 'Field Goal Persent', '3Point Field Goal Persent',
                    'Offensive Rebounds', 'Defensive Rebounds',
                    'Assists', 'Turnovers', 'Steals', 'Blocks']

        data = pd.DataFrame(result, columns=mycolumn)
        data.to_csv(self.chartname + '.csv', encoding='utf-8', index=False)

        print(self.chartname + '파일이 생성됨')