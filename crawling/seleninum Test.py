import time
from selenium import webdriver

# filename = '/home/junhwan/Downloads'
# driver = webdriver.Firefox(filename)

driver = webdriver.Firefox()

print(type(driver))  # WebDriver 객체
print('-' * 20)

print('네이버로 이동합니다.')
url = 'http://www.naver.com'
driver.get(url)

# name="q" 요소 찾기
search_textbox = driver.find_element_by_name('query')

word = '네이버'
search_textbox.send_keys(word)
search_textbox.submit()

driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div/div[1]/div/div[2]/a').click()


wait = 3
print(str(wait) + '동안 기다립니다.')
time.sleep(wait)

# imagefile = 'capture.png'
# driver.save_screenshot(imagefile)
# print(imagefile + ' 그림으로 저장합니다.')

wait = 3
driver.implicitly_wait(wait)

driver.quit()
print('brower를 종료합니다.')