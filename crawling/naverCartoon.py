import os
from pandas import DataFrame
from urllib.request import urlopen
from bs4 import BeautifulSoup

weekday_dict = {'mon':'월요일', 'tue':'화요일', 'wed':'수요일', 'thu':'목요일', 'fri':'금요일', 'sat':'토요일', 'sun':'일요일'}

# 촐더 경로를 myfolder에 저장
myfolder = '/home/junhwan/Work/python/imsi'


try:
    # 폴더가 없으면 폴더를 생성
    if not os.path.exists(myfolder):
        os.mkdir(myfolder)
        print('myfolder를 생성했습니다.')

    for mydir in weekday_dict.values():

        mypath = myfolder + '/' + mydir

        # 파일이 없으면 새로 생성하고 있으면 통과?
        if os.path.exists(mypath):
            pass
        else:
            os.mkdir(mypath)

except FileExistsError as err:
    pass

# 사이트의 이미지 파일을 해당 요일 폴더에 저장합니다.
def saveFile(mysrc, myweekday, mytitle):
   image_file = urlopen(mysrc)
   filename = myfolder + '/' + myweekday + '/' + mytitle + '.jpg'
   # print(filename)

   myfile = open(filename, mode='wb')
   # 바이너리 형태로 변경하여 기록합니다.
   myfile.write(image_file.read())
# print(weekday_dict)
# print('-'*30)
#
# print(weekday_dict.keys())
# print('-'*30)
#
# print(weekday_dict.values())
# print('-'*30)



#
# str = 'id=hong&password=1234'
#
# result = str.split('&')
# print(result)
#
# id=result[0].split('=')[1]
# password = result[1].split('=')[1]
#
# print("id:", id)
# print("password:", password)
#
# str2 = 'abc?:def'
# str2 = str2.replace('?','').replace(':','')
# print(str2)

myparse = 'html.parser'
myurl = 'https://comic.naver.com/webtoon/weekday.nhn'
response = urlopen(myurl)
# BeautifulSoup의 매개 변수는 2개이고 parse는 꼭 적어줘야 한다.
soup = BeautifulSoup(response, myparse)
print(type(soup)) # <class 'bs4.BeautifulSoup'> -> 출력이 되어야 정상

mytarget = soup.find_all('div', attrs={'class':'thumb'})
print('총 갯수: %d' % len(mytarget))

# 목록을 저장할 리스트
mylist = []

for abcd in mytarget:
   myhref = abcd.find('a').attrs['href']
   myhref = myhref.replace('/webtoon/list.nhn?', '')
   result = myhref.split('&')
   mytitleid = result[0].split('=')[1]
   myweekday = result[1].split('=')[1]
   myweekday = weekday_dict[myweekday]
   # print(mytitleid + '/' + myweekday)

   imgtag = abcd.find('img')
   mysrc = imgtag.attrs['src']

   # print(mysrc)

   mytitle = imgtag.attrs['title'].strip()
   mytitle = mytitle.replace('?','').replace('!','').replace(':','')

   # print(mytitle)

   mylist.append((mytitleid, myweekday, mytitle, mysrc))

   saveFile(mysrc, myweekday, mytitle)

print('리스트 내용 보기')
for i in range(len(mylist)):
    print(i, ":", mylist[i])

myframe = DataFrame(mylist, columns=['타이틀 번호', '요일', '제목', '링크'])
filename = 'cartoon.csv'
myframe.to_csv(filename, encoding='utf-8', index=False)

print('\n','finished')