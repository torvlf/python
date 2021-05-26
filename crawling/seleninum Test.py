import time
from selenium import webdriver

# filename = '/home/junhwan/Downloads'
# driver = webdriver.Firefox(filename)

driver = webdriver.Firefox()

print(type(driver))  # WebDriver 객체
print('-' * 20)

print('구글로 이동합니다.')
url = 'http://www.google.com'
driver.get(url)

# name="q" 요소 찾기
search_textbox = driver.find_element_by_name('q')

word = '북미정상회담'
search_textbox.send_keys(word)

search_textbox.submit()

wait = 3
print(str(wait) + '동안 기다립니다.')
time.sleep(wait)

imagefile = 'capture.png'
driver.save_screenshot(imagefile)
print(imagefile + ' 그림으로 저장합니다.')

wait = 3
driver.implicitly_wait(wait)

driver.quit()
print('brower를 종료합니다.')