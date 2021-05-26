#클래스
# 파이썬의 생성자는 __init__() 입니다.
# self 키워드는 객체 자신을 의미하는 용도로 사용됩니다.
# 반드시 작성해야 하며, 매개 변수로 입력할 필요 없습니다.

import datetime, ssl
import time
import urllib.request
import pandas as pd
from selenium import webdriver

from bs4 import BeautifulSoup

class ChickenStore():
    myencoding = 'utf-8'

    def __init__(self, brandName, url):
        self.brandName = brandName
        self.url = url

        if self.brandName != 'goobne':
            self.soup = self.get_request_url()
            self.driver = None
        else:
            # 굽네 매장일 때
            self.soup = None
            self.driver = webdriver.Firefox()
            self.driver.get(self.url)

    def get_request_url(self):
        request = urllib.request.Request(self.url)
        try:
            context = ssl._create_unverified_context()
            response = urllib.request.urlopen(request, context=context)
            if response.getcode() == 200:
                if self.brandName != 'pelicana':
                    return response.read().decode(self.myencoding)
                else:
                    return response

        except Exception as err:
            print(err)
            now = datetime.datetime.now()
            msg = '[%s] error for url %s' % (now, self.url)
            print(msg)
            return None

    def getSoup(self):
        if self.soup == None:
            return None
        else:
            if self.brandName != 'pelicana':
                return BeautifulSoup(self.soup, 'html.parser')
            else:
                return BeautifulSoup(self.soup, 'html.parser')

    def save2Csv(self, result):

        mycolumn = ['brand','store','sido','gungu','address','phone']

        data = pd.DataFrame(result, columns=mycolumn)
        data.to_csv(self.brandName + '.csv', encoding='utf-8', index=True)

        print(self.brandName + '파일이 생성됨')

    def getWebDriver(self, cmdJavaScript):
        print('cmdJavaScript: ',cmdJavaScript)
        self.driver.execute_script(cmdJavaScript)
        wait = 5
        # 5초 대기
        time.sleep(wait)
        mypage = self.driver.page_source
        # self.driver.quit()
        return BeautifulSoup(mypage, 'html.parser')