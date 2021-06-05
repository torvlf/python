import time
import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver

class KblGudan():
    myencoding = 'utf-8'

    def __init__(self, chartname, url):
        self.soup = None
        self.chartname = chartname
        self.url = url
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)

    def getWebDriver(self):
        wait = 10
        time.sleep(wait)
        mypage = self.driver.page_source
        return BeautifulSoup(mypage, 'html.parser')

    def save2Csv(self, result):

        mycolumn = ['GudanName', 'Sido', 'Gungu', 'Address']

        data = pd.DataFrame(result, columns=mycolumn)
        data.to_csv(self.chartname + '.csv', encoding='utf-8', index=False)

        print(self.chartname + '파일이 생성됨')